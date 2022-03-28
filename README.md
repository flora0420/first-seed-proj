![CI](https://github.com/flora0420/first-seed-proj/actions/workflows/ci.yml/badge.svg) 
![coverage](coverage.svg)
# first-seed-proj
Demo to create a python package using [python-seed](https://github.com/developmentseed/python-seed) with github CI setup.

Table of Contents
=================

* [first-seed-proj](#first-seed-proj)
   * [step by step instructions](#step-by-step-instructions)
      * [prerequisites](#prerequisites)
      * [Create the package using python-seed <strong>locally</strong>](#create-the-package-using-python-seed-locally)
      * [Repo / GitHub](#repo--github)
         * [Locally (<a href="https://kbroman.org/github_tutorial/pages/init.html" rel="nofollow">ref - create repo</a>)](#locally-ref---create-repo)
         * [On GitHub](#on-github)
         * [Connect it to GitHub](#connect-it-to-github)
      * [CI at work](#ci-at-work)
         * [Under the hood](#under-the-hood)
   * [Lessons Learned](#lessons-learned)
   * [Nice to Have](#nice-to-have)

## step by step instructions
### prerequisites
You can create an environment, optional but recommended.
```
pip install tox
pip install pytest
pip install python-seed
```

### Create the package using `python-seed` **locally**
create a new python project
```
pyseed create first-seed-proj --ci github
cd first-seed-proj
tree .
```
```
.
├── README.md
├── __pycache__
│   └── setup.cpython-39.pyc
├── first_seed_proj
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── app.cpython-39.pyc
│   └── app.py
├── codecov.yml
├── requirements-dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── test_function.cpython-39.pyc
│   │   └── test_mod.cpython-39.pyc
│   ├── test_function.py
│   └── test_mod.py
└── tox.ini
```
### Repo / GitHub
#### Locally ([ref - create repo](https://kbroman.org/github_tutorial/pages/init.html))
```
git init -b main # default branch master yet github/lab switched to main
git add .        # add files to staging
git commit -m 'create proj using pyseed' 
```

#### On GitHub
If you haven't used GitHub since Auguest 31, 2021, make sure to set up the [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) before proceed.

- create a new reprository named `first-seed-proj`
- add .gitignore using template for python
- choose a license (e.g., MIT)

#### Connect it to GitHub
([ref - merge conflict](https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase))
```
git remote add origin https://github.com/flora0420/first-seed-proj.git  
git remove -v                        # sanity check
git pull                             
git branch --set-upstream-to=origin/main main
git pull --allow-unrelated-histories # force merge to happen
```

using `tree` you'd see file LICENSE is now in your local repo, `ls -la` to verify that `.gitignore` exists.

now push all changes to remote. 
```
git push
```

### CI at work
Within a minute or two, one shall receive an email from GitHub soon titled `[flora0420/first-seed-proj] Run failed: CI - main`, click [View Workflow run](https://github.com/flora0420/first-seed-proj/actions/runs/2046791613), and see that the job has failed; specifically:

```
=================================== FAILURES ===================================
_________________________________ test_version _________________________________
    def test_version():
        """test version."""
>       assert first_seed_proj.version
E       AttributeError: module 'first_seed_proj' has no attribute 'version'
```

Fix the error in file `test_mode.py` and then push the changes.

#### Under the hood
1. [tox](https://tox.wiki/en/latest/index.html): automate and standardize testing in Python
    ```
    tox -e py
    ```
    locally and make sure all is clean before pushing changes. 
    ![tox workflow diagram](https://tox.wiki/en/latest/_images/tox_flow.png)
2. [pre-commit](https://pre-commit.com)
    ```
    arch -x86_64 brew install pre-commit # arch -x86_64 for m1
    # skip Add a pre-commit configuration as it's created by pyseed
    pre-commit install
    pre-commit run --all-files
    ```
    in VS Code, one can hold Command key ⌘ + Click/Tap on the link to the line where fix is needed. 

## Note
- [GitHub] features = branches. when trying a new feature, best practice is to work on a new branch named after the feature (or jira ticket id so that you could look it up in the system for more details). there are a few benefits:
    - avoid crowding the `main` branch while trial-and-erros 
    - streamline the code review with clear commit history 
    - parallel drawn from [merge vs rebase](https://betterprogramming.pub/differences-between-git-merge-and-rebase-and-why-you-should-care-ae41d96237b6)

- [Profiling] Profiling with `cProfile` and [`snakeviz`](https://jiffyclub.github.io/snakeviz/)
    ```
    python3 -m cProfile -o app.profile first_seed_proj/app.py
    python3 -m snakeviz app.profile   
    ```

- [Pytest DocTests] [Integration](https://doc.pytest.org/en/latest/how-to/doctest.html)
    - `pytest --doctest-modules`; 
    - make changes permanent in the project by putting them into a `pytest.ini` or `tox.ini` file [ref](https://stackoverflow.com/questions/17056138/how-to-make-pytest-run-doctests-as-well-as-normal-tests-directory)
        ```
        # content of pytest.ini
        [pytest]
        addopts = --doctest-modules
        ```
## Nice to Have
1. .gitignore and LICENSE should be created by default. [__pycache__](https://stackoverflow.com/questions/16869024/what-is-pycache) failed to be ignored as a result.
    - had to manually delete directories 
1. add the ci workflow status badge to README.md by default: [How-to](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
1. add [coverage badge](https://pypi.org/project/coverage-badge/)! 
    1. Generate coverage badges for Coverage.py.
        ```
        pip install coverage-badge
        coverage-badge -f -o coverage.svg # force override
        ```
    2. Add `![coverage](coverage.svg)` to the top of README.md
1. pages. It is a paid feature on GitHub. 
    - as a reference, when using gitlab, it is set in [`Python.gitlab-ci.yml`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Python.gitlab-ci.yml) as follows
    ```
    pages:
        script:
            - pip install sphinx sphinx-rtd-theme
            - cd doc
            - make html
            - mv build/html/ ../public/
        artifacts:
            paths:
            - public
        rules:
            - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
    ```
1. apparently, [cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/README.html) is more comphrensive.
1. once readme gets longer, how to add toc
    - [solution](https://github.com/ekalinin/github-markdown-toc)
    ```
    cd ../
    curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc -o gh-md-toc
    chmod a+x gh-md-toc
    ../gh-md-toc README.md # then copy and paste the output to readme.
    ```


## Further Reading
- [CI/CD by Example in Python](https://towardsdatascience.com/ci-cd-by-example-in-python-46f1533cb09d)
- [Setting up CI/CD for Python Packages using GitHub Actions](https://www.section.io/engineering-education/setting-up-cicd-for-python-packages-using-github-actions/#authenticating-github-with-test-pypi). Authenticating GitHub with Test PyPI is fun :) 