use serde::Serialize;
use anyhow::Result;
use tinytemplate::TinyTemplate;

// See: https://github.com/anuraghazra/github-readme-stats#customization
static PARAMS: &str = "username={user}&repo={repo}&theme=default&border_color={border_color}&bg_color={bg_color}&title_color={title_color}&text_color={text_color}&icon_color={icon_color}";
static README_CARD: &str = "[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?{params})](https://github.com/cjrh/{repo})";

#[derive(Serialize)]
struct Context {
    user: String,
    repo: String,
    border_color: String,
    bg_color: String,
    text_color: String,
    title_color: String,
    icon_color: String,
    params: String,
}

#[derive(Serialize)]
struct CardContext {
    params: String,
    repo: String,
}

static REPOS: &[&str] = &[
    "aiorun",
    "excitertools",
    "autoslot",
    "biodome",
    "coroexecutor",
    "aiomsg",
    "lifter",
    "easycython",
    "misu",
    "mucro",
    "itertree-rs",
];

static REPOS_LANGTOOLS: &[&str] = &[
    "dictomatic",
    "thesauromatic",
    "rhymomatic",
];

static REPOS_SMALLER: &[&str] = &[
    "pwrgen",
    "bumpymcbumpface",
    "clonymccloneface",
    "dockerctx",
    "aiohealthcheck",
    "templitz",
    "cjrh_template",
    "google-images-downloader",
];

static REPOS_LOGGING: &[&str] = &[
    "logjson",
    "loghandlerzmq",
    "logbind",
    "aiologfields",
    "arglog",
    "perflog",
    "sqllogformatter",
];

#[derive(Serialize)]
struct MainContext {
    REPOS: String,
    REPOS_LANGTOOLS: String,
    REPOS_SMALLER: String,
    REPOS_LOGGING: String,
}

fn main() -> Result<()> {
    let mut tt = tinytemplate::TinyTemplate::new();
    tt.set_default_formatter(&tinytemplate::format_unescaped);
    tt.add_template("params", PARAMS)?;
    tt.add_template("card", README_CARD)?;
    let readme = std::fs::read_to_string("README.md.template")?;
    tt.add_template("readme", &readme)?;

    let r1 = make_sec(&tt, REPOS)?;
    println!("{}", &r1);
    println!("\n\n");

    let r2 = make_sec(&tt, REPOS_LANGTOOLS)?;
    println!("{}", &r2);
    println!("\n\n");

    let r3 = make_sec(&tt, REPOS_SMALLER)?;
    println!("{}", &r3);
    println!("\n\n");

    let r4 = make_sec(&tt, REPOS_LOGGING)?;
    println!("{}", &r4);
    println!("\n\n");

    let ctx = MainContext {
        REPOS: r1,
        REPOS_LANGTOOLS: r2,
        REPOS_SMALLER: r3,
        REPOS_LOGGING: r4,
    };
    let output = tt.render("readme", &ctx)?;
    std::fs::write("README.md", output)?;

    Ok(())
}

fn make_sec(tt: &TinyTemplate, repos: &[&str]) -> Result<String> {
    let lines = repos.iter().map(|repo| process_repo(&tt, repo).expect("wat"));
    Ok(lines.collect::<Vec<_>>().join("\n"))
}


fn process_repo(tt: &TinyTemplate, repo: &str) -> Result<String> {
    let mut context = Context {
        user : "cjrh".to_string(),
        repo : repo.to_string(),
        border_color : "888888".to_string(),
        bg_color : "00000000".to_string(),
        title_color : "539af2".to_string(),
        icon_color : "888888".to_string(),
        text_color: "888888".to_string(),
        params: "".to_string(),
    };
    let params = tt.render("params", &context)?;
    // println!("{}", &params);

    // Update the context
    context.params = params;
    Ok(tt.render("card", &context)?)
}
