from ast import literal_eval
from string import Template
from dataclasses import dataclass, fields, asdict
from datetime import datetime, UTC
import sqlite3

GITHUB_DB = 'github.db'

@dataclass
class Repo:
    """Each of these fields corresponds to a column in the repos table"""
    name: str
    full_name: str
    private: bool
    html_url: str
    description: str
    fork: bool
    created_at: datetime
    updated_at: datetime
    stargazers_count: int
    language: str
    archived: bool
    open_issues_count: int
    license: str
    is_template: bool
    topics: list[str]
    visibility: str
    readme: str

    def __post_init__(self):
        # Change the created_at and updated_at fields to datetime objects
        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)

        if isinstance(self.updated_at, str):
            self.updated_at = datetime.fromisoformat(self.updated_at)

    def update_age(self):
        delta = datetime.now(UTC) - self.created_at
        # We want to formate this timedelta as the string "X years and Y months"
        fractional_years = delta.total_seconds() / 3600 / 24 / 365
        years = int(fractional_years)
        months = int((fractional_years - years) * 12)
        return f"{years} years and {months} months"

README_TEMPLATE = Template("""
# Welcome

## Links

- [GitHub](https://github.com/cjrh)
- [Mastodon](https://hachyderm.io/@caleb)
- ![Mastodon Follow](https://img.shields.io/mastodon/follow/108815314118110759?domain=hachyderm.io&style=flat)
- [Blog](https://tekmoji.com)
- [LinkedIn](https://www.linkedin.com/in/cjrh/)
- ![GitHub Sponsors](https://img.shields.io/github/sponsors/cjrh)
- ![GitHub followers](https://img.shields.io/github/followers/cjrh)
- ![GitHub User's stars](https://img.shields.io/github/stars/cjrh)
- ![Reddit User Karma](https://img.shields.io/reddit/user-karma/combined/caleb?style=flat)

## Projects

$repos

""")

# We're going to write special HTML for each project
# for a little more control over the style. We want them
# to look good! This HTML does need to work within the
# GitHub markdown renderer, though, and must follow Github
# rules.
PROJECT_MARKDOWN_README = Template("""
# $name ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
 
 <img 
        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" 
        style="vertical-align: middle;"
        alt="Python" width="32" height="32"/>
        
$description

This project is written in <strong>$language</strong>. It is $age years 
old, and has $stargazers_count stars on GitHub. These are the topics 
associated with this project: $topics
""")

shields = dict(
    commit_activity="![GitHub commit activity](https://img.shields.io/github/commit-activity/y/{user}/{repo})",
    contributors="![GitHub contributors](https://img.shields.io/github/contributors/{user}/{repo})",
    last_commit="![GitHub last commit](https://img.shields.io/github/last-commit/{cjrh}/{repo})",
    top_language="![GitHub top language](https://img.shields.io/github/languages/top/{cjrh}/{repo})",
    # ![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiorun)
    # ![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiorun)
    # ![PyPI - Downloads](https://img.shields.io/pypi/dm/aiorun)
    # ![GitHub License](https://img.shields.io/github/license/cjrh/aiorun)
    # ![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiorun)
    # ![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiorun)
    # ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiorun)
    # ![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/aiorun)
    # ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiorun)
    # ![GitHub forks](https://img.shields.io/github/forks/cjrh/aiorun)
    # ![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiorun)
    # ![PyPI - Version](https://img.shields.io/pypi/v/aiorun)

    # Rust
    # ![Crates.io Total Downloads](https://img.shields.io/crates/d/itertree)
    # ![Crates.io Dependents](https://img.shields.io/crates/dependents/playpen)
    # ![Crates.io Size](https://img.shields.io/crates/size/itertree)
    # ![Crates.io Version](https://img.shields.io/crates/v/itertree)
)

def main():
    conn = sqlite3.connect(GITHUB_DB)
    with conn:
        cur = conn.cursor()

        fieldnames = [f.name for f in fields(Repo)]
        joined = ', '.join(fieldnames)

        cur.execute(
            f'SELECT {joined} FROM repos '
            + f'where fork = 0 '
            + f'and archived = 0 '
            + f'and visibility = "public" '
            + f'and is_template = 0'
        )
        rows = cur.fetchall()

    # print(rows)

    repos = [Repo(*row) for row in rows]
    for repo in repos:
        repo.update_age()
    repos.sort(key=lambda r: r.stargazers_count, reverse=True)

    fragments = []
    for repo in repos:
        fragment = PROJECT_MARKDOWN_README.safe_substitute(
            {**asdict(repo), 'age': repo.update_age(),
             'topics':  ', '.join(
                f"""<a href="https://github.com/topics/{topic}" 
                style="border: 1px solid black; border-radius: 5px;">{topic}</a>"""
                 for topic in literal_eval(repo.topics)
             )}
        )
        fragments.append(fragment)

    document = README_TEMPLATE.safe_substitute(repos='\n'.join(fragments))
    print(document)


if __name__ == '__main__':
    main()
