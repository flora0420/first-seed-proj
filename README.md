#first-seed-proj
Demo to create a python package using [python-seed](https://github.com/developmentseed/python-seed) with github CI setup.

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
Locally ([ref - create repo](https://kbroman.org/github_tutorial/pages/init.html))
```
git init -b main # default branch master yet github/lab switched to main
git add .        # add files to staging
git commit -m 'create proj using pyseed' 
```

On GitHub
- create a new reprository named `first-seed-proj`
- add .gitignore using template for python
- choose a license (e.g., MIT)

Connect it to GitHub
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
Within a minute or two, you shall receive an email from GitHub titled `flora0420/first-seed-proj] Run failed: CI - main`, click [View Workflow run](https://github.com/flora0420/first-seed-proj/actions/runs/2046791613), and see that the job has failed; specifically:

```
=================================== FAILURES ===================================
_________________________________ test_version _________________________________
    def test_version():
        """test version."""
>       assert first_seed_proj.version
E       AttributeError: module 'first_seed_proj' has no attribute 'version'
```

Fix the error in file `test_mode.py` and then push the changes; 

#### tox
what should've done before pushing the changes is to run
```
tox -e py
```
locally and make sure all is clean before pushing changes. 

#### pre-commit
[officical website](https://pre-commit.com)
