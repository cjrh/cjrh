
I spend quite a lot of time on GitHub or on projects hosted on GitHub. These are my hobby projects,
although I use several of them also for work. There is no theme. From time to time an idea comes to
me and then I just "see what happens". I have a lot of fun with it. Some projects are more successful than others,
and some are much more fully developed than others; surprisingly, success and completeness are not
correlated.

I have many hobby projects. Over the years I have developed some habits that
reduce the time I need to spend on them. Time spent on project maintenance is time
not spent on playing with exciting new ideas and you can surely guess which
is my preference.

The most important habit is that I don't advertise these projects.
The projects are for me first and foremost. I am happy when
someone else finds them useful, but that's not the primary goal. Generally speaking,
once a project can do the thing I set out to achieve, I tend to avoid adding new
features. I do however try to fix bugs and keep the project up to date with
changes in the ecosystem.

Secondly, I try to keep dependencies to a minimum. My favorite hobby projects are
ones that depend only on the standard library; easier with Python than Rust but my orientation
is towards fewer when possible. I am
confident that these will work for a long time and with minimal input from me.
To be clear, I am not against
dependencies! I use many at work and I even wrote a book called "20 Python Libraries
You Aren't Using But Should". But for hobby projects, I want to keep the maintenance
burden as low as possible.

It isn't only code dependencies you
have to worry about: packaging in Python has been constantly shifting sand for many years,
release practices keep changing, and even CI also keeps changing every five years or so.
Before github actions I used AppVeyor and before that, travis-ci.
Once you have a few tens of projects, any small changes you have to do to all of them
starts to add up.
Over longer timeframes, all external dependencies change so the fewer the better.

Finally, I try to keep the project small in scope, and the code quality high.
Quality varies a lot on how long
I spend on the idea. I don't always succeed but I try. I
write tests, as much as I can, I track coverage, and I try to write detailed
documentation. The documentation is especially important because I even need it
myself to help remember why I did things a certain way several years ago.
Regression tests are very important if you're aiming for long-term reliability.

# Links About Me

- [Mastodon](https://hachyderm.io/@caleb)
- [Blog](https://tekmoji.com)
- [LinkedIn](https://www.linkedin.com/in/cjrh/)
- ![GitHub Sponsors](https://img.shields.io/github/sponsors/cjrh)
- ![GitHub followers](https://img.shields.io/github/followers/cjrh?style=flat)
- ![GitHub User's stars](https://img.shields.io/github/stars/cjrh?style=flat)

# Projects

The list of projects below excludes forks, archived repos, and toy experiments.
They are sorted in the following way:

- All projects with more than 10 stars are at the top.
- Projects less than 6 months old are the next group. (You probably don't want to
  use my older stuff)
- The rest appear below.

Each group is sorted by the number of stars. I don't especially care about
stars but they're useful as a proxy for "someone else finds this useful".

This way newer projects can be highlighted above very old projects that
might have a couple more stars.


<h2><a href="https://github.com/cjrh/aiorun">aiorun</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub License](https://img.shields.io/github/license/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiorun?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiorun)

A "run" function for asyncio-based apps that does all the boilerplate.

This project is written in <strong>Python</strong>. It is 7 years and 3 months years 
old, and has 445 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/async">async</a>, <a href="https://github.com/topics/async-await">async-await</a>, <a href="https://github.com/topics/asynchronous">asynchronous</a>, <a href="https://github.com/topics/asynchronous-tasks">asynchronous-tasks</a>, <a href="https://github.com/topics/asyncio">asyncio</a>, <a href="https://github.com/topics/asyncio-python">asyncio-python</a>


<h2><a href="https://github.com/cjrh/vim-conda">vim-conda</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub License](https://img.shields.io/github/license/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub forks](https://img.shields.io/github/forks/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![PyPI - Downloads](https://img.shields.io/pypi/dm/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/vim-conda?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fvim-conda)

Change conda environments in the Vim editor (with Jedi-vim support)

This project is written in <strong>Python</strong>. It is 9 years and 11 months years 
old, and has 111 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/conda-env">conda-env</a>, <a href="https://github.com/topics/conda-environment">conda-environment</a>, <a href="https://github.com/topics/jedi-vim">jedi-vim</a>, <a href="https://github.com/topics/python">python</a>, <a href="https://github.com/topics/vim">vim</a>, <a href="https://github.com/topics/vim-conda">vim-conda</a>


<h2><a href="https://github.com/cjrh/easycython">easycython</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub License](https://img.shields.io/github/license/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub forks](https://img.shields.io/github/forks/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![PyPI - Downloads](https://img.shields.io/pypi/dm/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/easycython?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Feasycython)

An easy way to convert a .pyx file into a .pyd file and avoid having to write a setup.py

This project is written in <strong>Python</strong>. It is 10 years and 6 months years 
old, and has 96 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/autoslot">autoslot</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub License](https://img.shields.io/github/license/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub forks](https://img.shields.io/github/forks/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![PyPI - Downloads](https://img.shields.io/pypi/dm/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/autoslot?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fautoslot)

Automatic __slots__ for your Python classes

This project is written in <strong>Python</strong>. It is 7 years and 3 months years 
old, and has 63 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/efficiency">efficiency</a>, <a href="https://github.com/topics/metaclass">metaclass</a>, <a href="https://github.com/topics/metaprogramming">metaprogramming</a>, <a href="https://github.com/topics/python">python</a>, <a href="https://github.com/topics/python-3">python-3</a>, <a href="https://github.com/topics/slots">slots</a>


<h2><a href="https://github.com/cjrh/thesauromatic">thesauromatic</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub License](https://img.shields.io/github/license/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub forks](https://img.shields.io/github/forks/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Crates.io Total Downloads](https://img.shields.io/crates/d/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Crates.io Dependents](https://img.shields.io/crates/dependents/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Crates.io Size](https://img.shields.io/crates/size/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)
![Crates.io Version](https://img.shields.io/crates/v/thesauromatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic)

Static, offline, command-line CLI thesaurus

This project is written in <strong>Rust</strong>. It is 6 years and 0 months years 
old, and has 18 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/cli-app">cli-app</a>, <a href="https://github.com/topics/language">language</a>, <a href="https://github.com/topics/thesaurus">thesaurus</a>


<h2><a href="https://github.com/cjrh/misu">misu</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub License](https://img.shields.io/github/license/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub forks](https://img.shields.io/github/forks/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![PyPI - Downloads](https://img.shields.io/pypi/dm/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/misu?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmisu)

High-speed physical quantities and dimensions in Python

This project is written in <strong>Python</strong>. It is 11 years and 7 months years 
old, and has 15 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/aiomsg">aiomsg</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub License](https://img.shields.io/github/license/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiomsg?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiomsg)

Smart sockets and scalability protocols for messaging network applications

This project is written in <strong>Python</strong>. It is 6 years and 9 months years 
old, and has 15 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/excitertools">excitertools</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub License](https://img.shields.io/github/license/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub forks](https://img.shields.io/github/forks/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![PyPI - Downloads](https://img.shields.io/pypi/dm/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/excitertools?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fexcitertools)

itertools (and more-itertools) in the form of function call chaining (fluent interface)

This project is written in <strong>Python</strong>. It is 4 years and 11 months years 
old, and has 14 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/chainable-methods">chainable-methods</a>, <a href="https://github.com/topics/fluent-interface">fluent-interface</a>, <a href="https://github.com/topics/itertools">itertools</a>, <a href="https://github.com/topics/itertools-library">itertools-library</a>, <a href="https://github.com/topics/pipeline-processor">pipeline-processor</a>


<h2><a href="https://github.com/cjrh/lifter">lifter</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub License](https://img.shields.io/github/license/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub forks](https://img.shields.io/github/forks/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Crates.io Total Downloads](https://img.shields.io/crates/d/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Crates.io Dependents](https://img.shields.io/crates/dependents/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Crates.io Size](https://img.shields.io/crates/size/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)
![Crates.io Version](https://img.shields.io/crates/v/lifter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flifter)

Download and sync new releases of single-file binaries from Github Releases and other sites

This project is written in <strong>Rust</strong>. It is 4 years and 4 months years 
old, and has 14 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/binaries">binaries</a>, <a href="https://github.com/topics/cli">cli</a>, <a href="https://github.com/topics/package-manager">package-manager</a>, <a href="https://github.com/topics/sync">sync</a>


<h2><a href="https://github.com/cjrh/deadpool">deadpool</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub License](https://img.shields.io/github/license/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub forks](https://img.shields.io/github/forks/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![PyPI - Downloads](https://img.shields.io/pypi/dm/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/deadpool?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdeadpool)

A Python Process Pool Executor implementation that is harder to break

This project is written in <strong>Python</strong>. It is 2 years and 4 months years 
old, and has 14 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/concurrent-futures">concurrent-futures</a>, <a href="https://github.com/topics/executor">executor</a>, <a href="https://github.com/topics/multiprocessing">multiprocessing</a>, <a href="https://github.com/topics/process-pool">process-pool</a>, <a href="https://github.com/topics/processpool">processpool</a>, <a href="https://github.com/topics/processpoolexecutor">processpoolexecutor</a>, <a href="https://github.com/topics/subprocess">subprocess</a>


<h2><a href="https://github.com/cjrh/coroexecutor">coroexecutor</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub License](https://img.shields.io/github/license/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub forks](https://img.shields.io/github/forks/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![PyPI - Downloads](https://img.shields.io/pypi/dm/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/coroexecutor?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcoroexecutor)

A CoroutineExecutor for asyncio, similar to nurseries and task groups

This project is written in <strong>Python</strong>. It is 5 years and 3 months years 
old, and has 13 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/asyncio">asyncio</a>, <a href="https://github.com/topics/coroutines">coroutines</a>, <a href="https://github.com/topics/taskgroup">taskgroup</a>, <a href="https://github.com/topics/taskgroups">taskgroups</a>


<h2><a href="https://github.com/cjrh/frisbee">frisbee</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub License](https://img.shields.io/github/license/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub forks](https://img.shields.io/github/forks/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Crates.io Total Downloads](https://img.shields.io/crates/d/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Crates.io Dependents](https://img.shields.io/crates/dependents/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Crates.io Size](https://img.shields.io/crates/size/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)
![Crates.io Version](https://img.shields.io/crates/v/frisbee?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ffrisbee)

Firefox automation

This project is written in <strong>Rust</strong>. It is 0 years and 5 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/cargo-generate-template-nostd-heapless">cargo-generate-template-nostd-heapless</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub License](https://img.shields.io/github/license/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub forks](https://img.shields.io/github/forks/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Crates.io Total Downloads](https://img.shields.io/crates/d/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Crates.io Dependents](https://img.shields.io/crates/dependents/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Crates.io Size](https://img.shields.io/crates/size/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)
![Crates.io Version](https://img.shields.io/crates/v/cargo-generate-template-nostd-heapless?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcargo-generate-template-nostd-heapless)

A cargo-generate template repo to start a no_std binary project using data structures from the heapless crate

This project is written in <strong>Rust</strong>. It is 0 years and 4 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/plenty">plenty</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub License](https://img.shields.io/github/license/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub forks](https://img.shields.io/github/forks/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Crates.io Total Downloads](https://img.shields.io/crates/d/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Crates.io Dependents](https://img.shields.io/crates/dependents/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Crates.io Size](https://img.shields.io/crates/size/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)
![Crates.io Version](https://img.shields.io/crates/v/plenty?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplenty)

Programming language

This project is written in <strong>Rust</strong>. It is 0 years and 2 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/playpen">playpen</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub License](https://img.shields.io/github/license/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub forks](https://img.shields.io/github/forks/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Crates.io Total Downloads](https://img.shields.io/crates/d/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Crates.io Dependents](https://img.shields.io/crates/dependents/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Crates.io Size](https://img.shields.io/crates/size/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)
![Crates.io Version](https://img.shields.io/crates/v/playpen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fplaypen)

Program launcher with memory and cpu limits

This project is written in <strong>Rust</strong>. It is 0 years and 1 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/cgr">cgr</a>, <a href="https://github.com/topics/cpu-limit">cpu-limit</a>, <a href="https://github.com/topics/memory-limit">memory-limit</a>, <a href="https://github.com/topics/systemd-run">systemd-run</a>


<h2><a href="https://github.com/cjrh/commas">commas</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub License](https://img.shields.io/github/license/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub forks](https://img.shields.io/github/forks/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Crates.io Total Downloads](https://img.shields.io/crates/d/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Crates.io Dependents](https://img.shields.io/crates/dependents/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Crates.io Size](https://img.shields.io/crates/size/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)
![Crates.io Version](https://img.shields.io/crates/v/commas?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcommas)

CLI tool to reformat text replacing whitespace with commas, or field template substitution

This project is written in <strong>Rust</strong>. It is 0 years and 0 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/cli">cli</a>, <a href="https://github.com/topics/pipeline">pipeline</a>, <a href="https://github.com/topics/shell">shell</a>


<h2><a href="https://github.com/cjrh/dockerctx">dockerctx</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub License](https://img.shields.io/github/license/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub forks](https://img.shields.io/github/forks/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/dockerctx?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdockerctx)

Context manager for managing the lifetime of a docker container

This project is written in <strong>Python</strong>. It is 7 years and 10 months years 
old, and has 8 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/docker">docker</a>, <a href="https://github.com/topics/python">python</a>, <a href="https://github.com/topics/unit-testing">unit-testing</a>


<h2><a href="https://github.com/cjrh/biodome">biodome</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub License](https://img.shields.io/github/license/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub forks](https://img.shields.io/github/forks/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![PyPI - Downloads](https://img.shields.io/pypi/dm/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/biodome?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome)

Better environment variables for Python

This project is written in <strong>Python</strong>. It is 7 years and 7 months years 
old, and has 8 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/environment-variables">environment-variables</a>, <a href="https://github.com/topics/environment-vars">environment-vars</a>


<h2><a href="https://github.com/cjrh/pyconau2018-arcade2Dmultiplayer">pyconau2018-arcade2Dmultiplayer</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" 
alt="Logo for programming language: javascript" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub License](https://img.shields.io/github/license/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub forks](https://img.shields.io/github/forks/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/pyconau2018-arcade2Dmultiplayer?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpyconau2018-arcade2Dmultiplayer)

Working files for my talk at PyCon AU 2018

This project is written in <strong>JavaScript</strong>. It is 6 years and 7 months years 
old, and has 6 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/google-images-downloader">google-images-downloader</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub License](https://img.shields.io/github/license/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub forks](https://img.shields.io/github/forks/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![PyPI - Downloads](https://img.shields.io/pypi/dm/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/google-images-downloader?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fgoogle-images-downloader)

An experiment in browser automation

This project is written in <strong>Python</strong>. It is 8 years and 9 months years 
old, and has 3 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/clonymccloneface">clonymccloneface</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub License](https://img.shields.io/github/license/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub forks](https://img.shields.io/github/forks/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Crates.io Total Downloads](https://img.shields.io/crates/d/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Crates.io Dependents](https://img.shields.io/crates/dependents/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Crates.io Size](https://img.shields.io/crates/size/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)
![Crates.io Version](https://img.shields.io/crates/v/clonymccloneface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fclonymccloneface)

Clone all your github repos AND set upstream for your forks

This project is written in <strong>Rust</strong>. It is 4 years and 5 months years 
old, and has 3 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/automation">automation</a>, <a href="https://github.com/topics/cloning">cloning</a>, <a href="https://github.com/topics/github-api">github-api</a>, <a href="https://github.com/topics/setup-development-environment">setup-development-environment</a>, <a href="https://github.com/topics/setup-tool">setup-tool</a>


<h2><a href="https://github.com/cjrh/debussy">debussy</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub License](https://img.shields.io/github/license/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub forks](https://img.shields.io/github/forks/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Crates.io Total Downloads](https://img.shields.io/crates/d/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Crates.io Dependents](https://img.shields.io/crates/dependents/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Crates.io Size](https://img.shields.io/crates/size/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)
![Crates.io Version](https://img.shields.io/crates/v/debussy?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdebussy)

CLI emitting json when song changes on Linux. Uses MPRIS and dbus to receive events

This project is written in <strong>Rust</strong>. It is 2 years and 2 months years 
old, and has 3 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/cli">cli</a>, <a href="https://github.com/topics/cli-app">cli-app</a>, <a href="https://github.com/topics/dbus">dbus</a>, <a href="https://github.com/topics/mpris">mpris</a>, <a href="https://github.com/topics/mpris-dbus-interface">mpris-dbus-interface</a>, <a href="https://github.com/topics/mpris2">mpris2</a>


<h2><a href="https://github.com/cjrh/mucro">mucro</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub License](https://img.shields.io/github/license/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub forks](https://img.shields.io/github/forks/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/mucro?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fmucro)

Easy executable symlinks to your virtualenv Python scripts

This project is written in <strong>Python</strong>. It is 7 years and 8 months years 
old, and has 2 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/aiodec">aiodec</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub License](https://img.shields.io/github/license/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiodec?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiodec)

Decorators for coroutines

This project is written in <strong>Python</strong>. It is 6 years and 10 months years 
old, and has 2 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/dialetto">dialetto</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub License](https://img.shields.io/github/license/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub forks](https://img.shields.io/github/forks/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Crates.io Total Downloads](https://img.shields.io/crates/d/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Crates.io Dependents](https://img.shields.io/crates/dependents/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Crates.io Size](https://img.shields.io/crates/size/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)
![Crates.io Version](https://img.shields.io/crates/v/dialetto?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdialetto)

Language detection. Finally one that works with short text.

This project is written in <strong>Rust</strong>. It is 3 years and 7 months years 
old, and has 2 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/biodome-rs">biodome-rs</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub License](https://img.shields.io/github/license/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub forks](https://img.shields.io/github/forks/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Crates.io Total Downloads](https://img.shields.io/crates/d/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Crates.io Dependents](https://img.shields.io/crates/dependents/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Crates.io Size](https://img.shields.io/crates/size/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)
![Crates.io Version](https://img.shields.io/crates/v/biodome-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbiodome-rs)

Neater management of environment variables (intended for microservices)

This project is written in <strong>Rust</strong>. It is 3 years and 6 months years 
old, and has 2 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/yet-another-python-indent">yet-another-python-indent</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vim/vim-original.svg" 
alt="Logo for programming language: vim" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub License](https://img.shields.io/github/license/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub forks](https://img.shields.io/github/forks/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/yet-another-python-indent?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fyet-another-python-indent)

Back to basics indentexpr for Python

This project is written in <strong>Vim Script</strong>. It is 0 years and 6 months years 
old, and has 2 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/indent">indent</a>, <a href="https://github.com/topics/indentation">indentation</a>, <a href="https://github.com/topics/indentexpr">indentexpr</a>, <a href="https://github.com/topics/neovim-plugin">neovim-plugin</a>, <a href="https://github.com/topics/python-indent">python-indent</a>, <a href="https://github.com/topics/vim-plugin">vim-plugin</a>


<h2><a href="https://github.com/cjrh/copydir">copydir</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub License](https://img.shields.io/github/license/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub forks](https://img.shields.io/github/forks/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![PyPI - Downloads](https://img.shields.io/pypi/dm/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/copydir?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcopydir)

Recursively copy a directory tree, with filters.

This project is written in <strong>Python</strong>. It is 9 years and 11 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/sqllogformatter">sqllogformatter</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub License](https://img.shields.io/github/license/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub forks](https://img.shields.io/github/forks/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![PyPI - Downloads](https://img.shields.io/pypi/dm/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/sqllogformatter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fsqllogformatter)

A Python logging Formatter subclass for messages with SQL queries

This project is written in <strong>Python</strong>. It is 8 years and 1 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/cjrh_template">cjrh_template</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub License](https://img.shields.io/github/license/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub forks](https://img.shields.io/github/forks/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/cjrh_template?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_template)

A very thin string.Template subclass with extra features.

This project is written in <strong>Python</strong>. It is 7 years and 8 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/aiologfields">aiologfields</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub License](https://img.shields.io/github/license/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiologfields?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiologfields)

Automatically inject Task-context-aware fields into loggers

This project is written in <strong>Python</strong>. It is 7 years and 1 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/bumpymcbumpface">bumpymcbumpface</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub License](https://img.shields.io/github/license/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub forks](https://img.shields.io/github/forks/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/bumpymcbumpface?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fbumpymcbumpface)

Version bump, tag and deploy your python packages

This project is written in <strong>Python</strong>. It is 5 years and 8 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/automation">automation</a>, <a href="https://github.com/topics/bump-version">bump-version</a>, <a href="https://github.com/topics/bumpversion">bumpversion</a>, <a href="https://github.com/topics/deploy">deploy</a>, <a href="https://github.com/topics/pypi">pypi</a>, <a href="https://github.com/topics/release">release</a>, <a href="https://github.com/topics/tagging">tagging</a>


<h2><a href="https://github.com/cjrh/dictomatic">dictomatic</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub License](https://img.shields.io/github/license/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub forks](https://img.shields.io/github/forks/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Crates.io Total Downloads](https://img.shields.io/crates/d/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Crates.io Dependents](https://img.shields.io/crates/dependents/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Crates.io Size](https://img.shields.io/crates/size/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)
![Crates.io Version](https://img.shields.io/crates/v/dictomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdictomatic)

Static, offline, command-line CLI dictionary (including word definitions)

This project is written in <strong>Rust</strong>. It is 5 years and 1 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/empatico">empatico</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub License](https://img.shields.io/github/license/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub forks](https://img.shields.io/github/forks/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![PyPI - Downloads](https://img.shields.io/pypi/dm/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/empatico?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fempatico)

Emotion detection microservice based on natural language inference

This project is written in <strong>Python</strong>. It is 3 years and 3 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/emotion-detection">emotion-detection</a>, <a href="https://github.com/topics/mnli">mnli</a>, <a href="https://github.com/topics/natural-language-inference">natural-language-inference</a>, <a href="https://github.com/topics/natural-language-processing">natural-language-processing</a>, <a href="https://github.com/topics/sentiment-analysis">sentiment-analysis</a>, <a href="https://github.com/topics/sentiment-classification">sentiment-classification</a>


<h2><a href="https://github.com/cjrh/scalable-cuckoo-filter-py">scalable-cuckoo-filter-py</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub License](https://img.shields.io/github/license/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub forks](https://img.shields.io/github/forks/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![PyPI - Downloads](https://img.shields.io/pypi/dm/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/scalable-cuckoo-filter-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fscalable-cuckoo-filter-py)

Python wrapper for sile/scalable_cuckoo_filter

This project is written in <strong>Rust</strong>. It is 0 years and 6 months years 
old, and has 1 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/cjrh.github.io">cjrh.github.io</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original.svg" 
alt="Logo for programming language: jupyter" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub License](https://img.shields.io/github/license/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub forks](https://img.shields.io/github/forks/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/cjrh.github.io?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh.github.io)

My blog 🤷

This project is written in <strong>Jupyter Notebook</strong>. It is 11 years and 3 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/pathprinter">pathprinter</a> </h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub License](https://img.shields.io/github/license/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub forks](https://img.shields.io/github/forks/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/pathprinter?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpathprinter)

Prints out the windows %PATH% variable as a list

This project is written in <strong>Pascal</strong>. It is 10 years and 2 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/arglog">arglog</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub License](https://img.shields.io/github/license/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub forks](https://img.shields.io/github/forks/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![PyPI - Downloads](https://img.shields.io/pypi/dm/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/arglog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Farglog)

Add root logger config to argparse automatically

This project is written in <strong>Python</strong>. It is 7 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/argument-parser">argument-parser</a>, <a href="https://github.com/topics/logging">logging</a>


<h2><a href="https://github.com/cjrh/logbind">logbind</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub License](https://img.shields.io/github/license/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub forks](https://img.shields.io/github/forks/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![PyPI - Downloads](https://img.shields.io/pypi/dm/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/logbind?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogbind)

Easily bind new LogRecord fields into your logger instances.

This project is written in <strong>Python</strong>. It is 7 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/perflog">perflog</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub License](https://img.shields.io/github/license/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub forks](https://img.shields.io/github/forks/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![PyPI - Downloads](https://img.shields.io/pypi/dm/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/perflog?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fperflog)

Structured logging support for application performance and monitoring data

This project is written in <strong>Python</strong>. It is 7 years and 5 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/logging">logging</a>, <a href="https://github.com/topics/monitor-performance">monitor-performance</a>, <a href="https://github.com/topics/monitoring">monitoring</a>


<h2><a href="https://github.com/cjrh/templitz">templitz</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub License](https://img.shields.io/github/license/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub forks](https://img.shields.io/github/forks/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![PyPI - Downloads](https://img.shields.io/pypi/dm/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/templitz?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Ftemplitz)

File templates for faster project bootstrap

This project is written in <strong>Python</strong>. It is 7 years and 3 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/cjrh_math">cjrh_math</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub License](https://img.shields.io/github/license/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub forks](https://img.shields.io/github/forks/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/cjrh_math?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh_math)

Handy math routines

This project is written in <strong>Python</strong>. It is 7 years and 2 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/logjson">logjson</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub License](https://img.shields.io/github/license/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub forks](https://img.shields.io/github/forks/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![PyPI - Downloads](https://img.shields.io/pypi/dm/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/logjson?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flogjson)

A Python logging Handler for JSON logs (with LogStash support)

This project is written in <strong>Python</strong>. It is 7 years and 2 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/aiohealthcheck">aiohealthcheck</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub License](https://img.shields.io/github/license/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/aiohealthcheck?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faiohealthcheck)

Very simple TCP-based health check service. 

This project is written in <strong>Python</strong>. It is 7 years and 1 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/ps1go">ps1go</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg" 
alt="Logo for programming language: go" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub License](https://img.shields.io/github/license/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub forks](https://img.shields.io/github/forks/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/ps1go?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fps1go)

PS1 prompt generator

This project is written in <strong>Go</strong>. It is 6 years and 9 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/pwrgen">pwrgen</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub License](https://img.shields.io/github/license/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub forks](https://img.shields.io/github/forks/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Crates.io Total Downloads](https://img.shields.io/crates/d/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Crates.io Dependents](https://img.shields.io/crates/dependents/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Crates.io Size](https://img.shields.io/crates/size/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)
![Crates.io Version](https://img.shields.io/crates/v/pwrgen?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fpwrgen)

Password and passphrase generator in rust

This project is written in <strong>Rust</strong>. It is 6 years and 2 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/loghandlerzmq">loghandlerzmq</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub License](https://img.shields.io/github/license/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub forks](https://img.shields.io/github/forks/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![PyPI - Downloads](https://img.shields.io/pypi/dm/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/loghandlerzmq?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Floghandlerzmq)

Python logging handler for ZMQ transmission

This project is written in <strong>Python</strong>. It is 5 years and 9 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/enumerate_reversible">enumerate_reversible</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub License](https://img.shields.io/github/license/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub forks](https://img.shields.io/github/forks/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![PyPI - Downloads](https://img.shields.io/pypi/dm/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/enumerate_reversible?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fenumerate_reversible)

A replacement enumerate function that allows reverse order

This project is written in <strong>Python</strong>. It is 4 years and 9 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/covcompare">covcompare</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub License](https://img.shields.io/github/license/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub forks](https://img.shields.io/github/forks/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Crates.io Total Downloads](https://img.shields.io/crates/d/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Crates.io Dependents](https://img.shields.io/crates/dependents/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Crates.io Size](https://img.shields.io/crates/size/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)
![Crates.io Version](https://img.shields.io/crates/v/covcompare?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcovcompare)

Compare two xml coverage files, report on branch and line coverage

This project is written in <strong>Rust</strong>. It is 3 years and 11 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/rhymomatic">rhymomatic</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub License](https://img.shields.io/github/license/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub forks](https://img.shields.io/github/forks/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Crates.io Total Downloads](https://img.shields.io/crates/d/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Crates.io Dependents](https://img.shields.io/crates/dependents/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Crates.io Size](https://img.shields.io/crates/size/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)
![Crates.io Version](https://img.shields.io/crates/v/rhymomatic?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Frhymomatic)

Static, offline, command-line rhyming dictionary

This project is written in <strong>Rust</strong>. It is 3 years and 8 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/alliteration">alliteration</a>, <a href="https://github.com/topics/pairing">pairing</a>, <a href="https://github.com/topics/perfect-rhymes">perfect-rhymes</a>


<h2><a href="https://github.com/cjrh/itertree-rs">itertree-rs</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub License](https://img.shields.io/github/license/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub forks](https://img.shields.io/github/forks/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Crates.io Total Downloads](https://img.shields.io/crates/d/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Crates.io Dependents](https://img.shields.io/crates/dependents/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Crates.io Size](https://img.shields.io/crates/size/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)
![Crates.io Version](https://img.shields.io/crates/v/itertree-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fitertree-rs)

Hobby project exploring tree traversal in Rust using iterators

This project is written in <strong>Rust</strong>. It is 3 years and 8 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/cjrh">cjrh</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub License](https://img.shields.io/github/license/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub forks](https://img.shields.io/github/forks/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Crates.io Total Downloads](https://img.shields.io/crates/d/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Crates.io Dependents](https://img.shields.io/crates/dependents/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Crates.io Size](https://img.shields.io/crates/size/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)
![Crates.io Version](https://img.shields.io/crates/v/cjrh?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fcjrh)

This generates the README.md for my github profile, which is likely what you're currently reading.

This project is written in <strong>Rust</strong>. It is 3 years and 7 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/readme">readme</a>, <a href="https://github.com/topics/readme-gen">readme-gen</a>, <a href="https://github.com/topics/readme-generator">readme-generator</a>, <a href="https://github.com/topics/readme-md">readme-md</a>, <a href="https://github.com/topics/readme-profile">readme-profile</a>


<h2><a href="https://github.com/cjrh/thesauromatic-py">thesauromatic-py</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub License](https://img.shields.io/github/license/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub forks](https://img.shields.io/github/forks/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![PyPI - Downloads](https://img.shields.io/pypi/dm/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/thesauromatic-py?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fthesauromatic-py)

Python wrapper for my "thesauromatic" library.

This project is written in <strong>Rust</strong>. It is 3 years and 3 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/pyo3-rust-bindings">pyo3-rust-bindings</a>, <a href="https://github.com/topics/python-wrapper">python-wrapper</a>, <a href="https://github.com/topics/thesaurus">thesaurus</a>


<h2><a href="https://github.com/cjrh/aggonydb">aggonydb</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub License](https://img.shields.io/github/license/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub forks](https://img.shields.io/github/forks/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Crates.io Total Downloads](https://img.shields.io/crates/d/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Crates.io Dependents](https://img.shields.io/crates/dependents/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Crates.io Size](https://img.shields.io/crates/size/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)
![Crates.io Version](https://img.shields.io/crates/v/aggonydb?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Faggonydb)

Aggony DB is a one-trick-pony database that can perform rapid aggregation of many-fields low-cardinality big data

This project is written in <strong>Rust</strong>. It is 2 years and 9 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/aggregation">aggregation</a>, <a href="https://github.com/topics/datasketches">datasketches</a>, <a href="https://github.com/topics/probabilistic-data-structures">probabilistic-data-structures</a>


<h2><a href="https://github.com/cjrh/dining-philosophers">dining-philosophers</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub License](https://img.shields.io/github/license/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub forks](https://img.shields.io/github/forks/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Crates.io Total Downloads](https://img.shields.io/crates/d/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Crates.io Dependents](https://img.shields.io/crates/dependents/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Crates.io Size](https://img.shields.io/crates/size/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)
![Crates.io Version](https://img.shields.io/crates/v/dining-philosophers?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fdining-philosophers)

The "Dining Philosophers" problem

This project is written in <strong>Rust</strong>. It is 1 years and 4 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/nnsplit-unblocked">nnsplit-unblocked</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub License](https://img.shields.io/github/license/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub forks](https://img.shields.io/github/forks/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Crates.io Total Downloads](https://img.shields.io/crates/d/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Crates.io Dependents](https://img.shields.io/crates/dependents/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Crates.io Size](https://img.shields.io/crates/size/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)
![Crates.io Version](https://img.shields.io/crates/v/nnsplit-unblocked?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fnnsplit-unblocked)

A python wrapper for nnsplit 0.5.9 that runs in newer python versions

This project is written in <strong>Rust</strong>. It is 0 years and 7 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/hashdict">hashdict</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
alt="Logo for programming language: python" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub License](https://img.shields.io/github/license/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub forks](https://img.shields.io/github/forks/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)
![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/hashdict?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fhashdict)

Dict that only stores hashes of the keys, and not the key value. Good for large keys.

This project is written in <strong>Python</strong>. It is 0 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/linedance">linedance</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub License](https://img.shields.io/github/license/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub forks](https://img.shields.io/github/forks/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Crates.io Total Downloads](https://img.shields.io/crates/d/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Crates.io Dependents](https://img.shields.io/crates/dependents/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Crates.io Size](https://img.shields.io/crates/size/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)
![Crates.io Version](https://img.shields.io/crates/v/linedance?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Flinedance)

Read lines from either stdin or filenames provided on the CLI.

This project is written in <strong>Rust</strong>. It is 0 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 


<h2><a href="https://github.com/cjrh/acts">acts</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub License](https://img.shields.io/github/license/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub forks](https://img.shields.io/github/forks/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Crates.io Total Downloads](https://img.shields.io/crates/d/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Crates.io Dependents](https://img.shields.io/crates/dependents/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Crates.io Size](https://img.shields.io/crates/size/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)
![Crates.io Version](https://img.shields.io/crates/v/acts?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Facts)

Small terminal menu to run preconfigured commands

This project is written in <strong>Rust</strong>. It is 0 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: <a href="https://github.com/topics/command-line-interface">command-line-interface</a>, <a href="https://github.com/topics/command-runner">command-runner</a>, <a href="https://github.com/topics/terminal-based">terminal-based</a>, <a href="https://github.com/topics/terminal-menu">terminal-menu</a>


<h2><a href="https://github.com/cjrh/terminal-menu-rs">terminal-menu-rs</a> <img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/rust/rust-original.svg" 
alt="Logo for programming language: rust" width="32" height="32"
style="vertical-align: middle;"
/></h2>

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub contributors](https://img.shields.io/github/contributors/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub last commit](https://img.shields.io/github/last-commit/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub top language](https://img.shields.io/github/languages/top/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Coveralls](https://img.shields.io/coverallsCoverage/github/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub License](https://img.shields.io/github/license/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub forks](https://img.shields.io/github/forks/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![GitHub Repo stars](https://img.shields.io/github/stars/cjrh/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Crates.io Total Downloads](https://img.shields.io/crates/d/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Crates.io Dependents](https://img.shields.io/crates/dependents/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Crates.io Size](https://img.shields.io/crates/size/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)
![Crates.io Version](https://img.shields.io/crates/v/terminal-menu-rs?style=flat&link=https%3A%2F%2Fgithub.com%2Fcjrh%2Fterminal-menu-rs)

THIS IS NOT UPSTREAM! Forked from gitlab: https://gitlab.com/xamn/terminal-menu-rs

This project is written in <strong>Rust</strong>. It is 0 years and 6 months years 
old, and has 0 stars on GitHub. These are the topics 
associated with this project: 



