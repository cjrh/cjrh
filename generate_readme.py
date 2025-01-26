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
- ![GitHub followers](https://img.shields.io/github/followers/cjrh?style=flat)
- ![GitHub User's stars](https://img.shields.io/github/stars/cjrh?style=flat)

## Projects

$repos

""")
# - ![Reddit User Karma](https://img.shields.io/reddit/user-karma/combined/caleb?style=flat)

# We're going to write special HTML for each project
# for a little more control over the style. We want them
# to look good! This HTML does need to work within the
# GitHub markdown renderer, though, and must follow Github
# rules.
PROJECT_MARKDOWN_README = Template("""
<h1><a href="https://github.com/$user/$name">$name</a> $lang_image</h1>

$shields_text
        
$description

This project is written in <strong>$language</strong>. It is $age years 
old, and has $stargazers_count stars on GitHub. These are the topics 
associated with this project: $topics
""")

lang_image = """<img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{language}/{language}-original.svg" 
alt="Logo for programming language: {language}" width="32" height="32"
style="vertical-align: middle;"
/>"""

shields_style = "?style={style}&link=https%3A%2F%2Fgithub.com%2F{user}%2F{repo}"

shields = dict(
    commit_activity="![GitHub commit activity](https://img.shields.io/github/commit-activity/y/{user}/{repo}",
    contributors="![GitHub contributors](https://img.shields.io/github/contributors/{user}/{repo}",
    last_commit="![GitHub last commit](https://img.shields.io/github/last-commit/{user}/{repo}",
    top_language="![GitHub top language](https://img.shields.io/github/languages/top/{user}/{repo}",
    coveralls="![Coveralls](https://img.shields.io/coverallsCoverage/github/{user}/{repo}",
    github_dependency_status="![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/{user}/{repo}",
    github_license="![GitHub License](https://img.shields.io/github/license/{user}/{repo}",
    # sourcerank="![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/{repo}",
    github_code_size="![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/{user}/{repo}",
    forks="![GitHub forks](https://img.shields.io/github/forks/{user}/{repo}",
    stars="![GitHub Repo stars](https://img.shields.io/github/stars/{user}/{repo}",
)
shields = {key: value + shields_style + ")" for key, value in shields.items()}

python_shields = dict(
    pypi_downloads="![PyPI - Downloads](https://img.shields.io/pypi/dm/{repo}",
    pypi_version="![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{repo}",
    # ![PyPI - Version](https://img.shields.io/pypi/v/{repo})
    dependent_repos="![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/{repo}",
    dependent_libs="![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/{repo}",
    coveralls="![Coveralls](https://img.shields.io/coverallsCoverage/github/{user}/{repo}",
)
python_shields = {key: value + shields_style + ")" for key, value in python_shields.items()}

rust_shields = dict(
    total_downloads="![Crates.io Total Downloads](https://img.shields.io/crates/d/{repo}",
    crates_dependents="![Crates.io Dependents](https://img.shields.io/crates/dependents/{repo}",
    crates_size="![Crates.io Size](https://img.shields.io/crates/size/{repo}",
    crates_version="![Crates.io Version](https://img.shields.io/crates/v/{repo}",
)
rust_shields = {key: value + shields_style + ")" for key, value in rust_shields.items()}

exclusions = {
    "osx-finder-toolbar-apps",
    "sqlite-server",
    "brispy-cython-workshop",
    "chat",
    "chained-iterable",
    "linux-toolbox-gui",
    "postgres_crud_generator",
    "cgroup_executor",
    "termtheme",
    "lizard",
    "adventofcode2021",
    "actix-sse-demo",
}

def main():
    conn = sqlite3.connect(GITHUB_DB)
    with conn:
        cur = conn.cursor()

        fieldnames = [f.name for f in fields(Repo)]
        joined = ', '.join(fieldnames)

        # We want to order the output in a very particular way:
        # If the age is less than 1 year, we want all of those to sort
        # to the top, and in order of stargazers_count. If the age
        # is older than 1 year, we want to sort by stargazers_count.
        cur.execute(f"""
            SELECT {joined} FROM repos
            where fork = 0
            and archived = 0
            and visibility = 'public'
            and is_template = 0
            order by
                case
                    when stargazers_count > 10 then stargazers_count + 100000
                    when julianday('now') - julianday(created_at) < 186 then stargazers_count + 10000
                    else stargazers_count
                end desc
        """)
        rows = cur.fetchall()

    # print(rows)


    repos = [Repo(*row) for row in rows]
    for repo in repos:
        repo.update_age()
    # repos.sort(key=lambda r: r.stargazers_count, reverse=True)

    fragments = []
    for repo in repos:
        if repo.name in exclusions:
            continue

        context = {
            **asdict(repo),
            "user": "cjrh",
            "repo": repo.name,
            "style": "flat",
        }

        if repo.language:
            value = repo.language.lower()
            if value == "jupyter notebook":
                value = "jupyter"
            elif value == "vim script":
                value = "vim"

            if value == "pascal":
                lang_image_text = ""
            else:
                lang_image_text = lang_image.format(language=value)
        else:
            lang_image_text = ""

        shields_to_process = shields
        # Also handle Python wrappers for rust crates
        if repo.language == "Python" or repo.name.lower().endswith("py"):
            shields_to_process = {**shields_to_process, **python_shields}
        elif repo.language == "Rust":
            shields_to_process = {**shields_to_process, **rust_shields}

        shields_text = "\n".join(
            value.format(**context)
            for key, value in shields_to_process.items()
        )

        fragment = PROJECT_MARKDOWN_README.safe_substitute(
            {
                "user": "cjrh",
                "repo": repo.name,
                **asdict(repo),
                'age': repo.update_age(),
                 'topics':  ', '.join(
                    f"""<a href="https://github.com/topics/{topic}">{topic}</a>"""
                     for topic in literal_eval(repo.topics)
                 ),
                'lang_image': lang_image_text,
                'shields_text': shields_text,
            }
        )
        fragments.append(fragment)

    document = README_TEMPLATE.safe_substitute(repos='\n'.join(fragments))
    print(document)


if __name__ == '__main__':
    main()
