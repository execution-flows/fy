# Fy Library


_Fy Library_ is the core functional part of the `fy` tool. It contains code for discovering and parsing `fy` code, then generating resulting Python code. 

## Setting up local development

We develop the `fy` tool using the very same `fy` tool. But we cannot use the same copy that we use for development to transform edited `fy` files because files break during development.

For that purpose of avoiding breaking the very same tool that we use for development, we clone another repo that we use as a source code for running the `fy` cli tool.

### 1. Clone the repo once more to serve as a local `fy` cli tool

Clone the same `fy` repo once more in the `local-fy-cli` folder adjacent to this project folder. FYI, the second parameter in `git clone` is the directory to clone the repo in like:

```shell
git clone git@github.com:execution-flows/fy.git local-fy-cli
```

After cloning the repo your directory structure should be like:
```
├── fy
│   ├── cli
│   ├── documentation_site
│   ├── library
│   ├── local.fy.sh
├── local-fy-cli
│   ├── cli
│   ├── documentation_site
│   ├── library
│   ├── local.fy.sh
```

### 2. Set up `poetry` in the `local-fy-cli/cli` directory

```shell
cd local-fy-cli/cli
poetry env use 3.10
poetry install
```

### 3. Run the `local.fy.sh` to execute the tool

In the project root folder

```shell
./local.fy.sh
```

**NOTE:** `local.fy.sh` is configured with `/library/src` as a project root folder, so only files in that folder can be processed with it. 

### 4. \[Optional] Set up external tool in PyCharm

1. PyCharm -> Settings -> Tools -> External Tools
2. '+' (or Add) to create a new tool
3. Fill in:

   - Name: `local fy`
   - Program: \<path to local.fy.sh>
   - Arguments: `$FileDir$`
   - Working directory: \<path to /library/src>

Now you can run the tool by selecting `Tools -> External Tools -> local fy`, or option-click on a file or folder and choose `External Tools -> local fy`.  

To speed things up you can assign a keyboard shortcut to it in `PyCharm -> Settings -> Keymap -> External Tools -> External Tools -> local fy`. Then click on pencil at the top, and select `Add Keyboard Shortcut`. 

### Important: keep `local-fy-cli` up to date.

Regularly, as often as you do with the primary development `fy` repo, run `git pull origin main` in the `local-fy-cli` repo. 

## Testing 

The main principle of `fy` tool development is Test-Driven-Development. The level of tests we use for development is the integration level.

The integration test in this project means writing the `fy` code, and comparing the generated Python code with the expected Python code.

To run the tests from `poetry shell` use the following command:

```shell
poetry run python -m unittest
```

## Set-up code formatting, linting, and type checks

Use the poetry shell from the root project.

```shell
poetry env use 3.10
poetry install
```

We use `pre-commit` to run a bunch of checks before committing to git, if you want to run these checks at any time, on all files you can use

```shell
poetry run pre-commit run -a
```
