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
# Projects

$data

""")

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

    with open("generated_links.md") as f:
        lines = f.readlines()

    lines = [
        line for line in lines
        if not any(exclusion in line for exclusion in exclusions)
    ]

    lines.sort()
    document = README_TEMPLATE.safe_substitute(data=''.join(lines))
    print(document)


if __name__ == '__main__':
    main()
