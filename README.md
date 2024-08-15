This repo is organized as a monorepo. Each folder is its own project and contains own `README.md`.

## Set-up code formatting, linting, and type checks

Use the poetry shell from the `library` project.

```shell
cd library
poetry shell
```

Install `pre-commit` if you don't have it already. Visit the official web for installation instructions: [pre-commit.com](https://pre-commit.com)

```shell
pip install pre-commit
```

All `pre-commit` commands should be executed from the root repo directory. 
```shell
cd ..
```

The first time you clone this repo, you'll have to run:

```shell
pre-commit install
```

We use `pre-commit` to run a bunch of checks before committing to git, if you want to run these checks at any time, on all files you can use

```shell
pre-commit run -a
```

If you get `mypy` warnings regarding missing packages, it's usually because dependencies need to be also added to `.pre-commit-config.yaml` (annoying, I know, but it seems to be the way to go for now)


