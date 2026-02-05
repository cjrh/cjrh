@default:
    just -l

update-repos:
    github-to-sqlite repos github.db cjrh --readme --readme-html

regen:
    python generate_readme.py > README.md

gen-links:
    gh repo list --limit 1000 --no-archived --source --visibility public --json name,url,description -q '.[] | "- [\(.name)](\(.url)): \(.description)"' > generated_links.md
