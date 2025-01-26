@default:
    just -l

update-repos:
    github-to-sqlite repos github.db cjrh --readme --readme-html

regen:
    python generate_readme.py > README.md
