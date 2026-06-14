@default:
    just -l

update-repos:
    github-to-sqlite repos github.db cjrh --readme --readme-html

# Refuse to overwrite the hand-authored profile README.
regen:
    @echo "README.md is hand-authored now; edit it directly instead of regenerating it."
    @exit 1

gen-links:
    gh repo list --limit 1000 --no-archived --source --visibility public --json name,url,description -q '.[] | "- [\(.name)](\(.url)): \(.description)"' > generated_links.md
