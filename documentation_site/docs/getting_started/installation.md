The ___fy___ tool is not currently released as a Python package installable from pypi.org or similar package repository. It has to be used by cloning the `fy` repository locally and executed directly.

### 1. Clone the Repo for Local ___fy___ CLI Tool

Clone the `fy` repository:

```bash
git clone git@github.com:execution-flows/fy.git
```
### 2. Set Up Poetry in the fy/cli Directory

If you do not have `poetry` installed, it is as simple as `pipx install poetry` - [Poetry documentation](https://python-poetry.org/docs/).

Navigate to the `fy/cli` directory and set up the Python environment using Poetry:

```bash
cd fy/cli
```
```bash
poetry env use 3.10
poetry install
```

!!! info
    The ___fy___ tool also supports Python 3.11 and 3.12. If you do not have Python 3.10 installed, change `poetry env use` to a version that you have installed.

### 3. Run the `fy.sh` Script

Use your project's source root directory as a working directory and run the `fy/fy.sh` script.

```bash
<path toward fy directory>/fy/fy.sh
```

!!! info
    It is important to run the `fy/fy.sh` script from your source root directory since the script is taking the working directory as the Python project root and generating Python imports based on that directory.

It is a good practice to connect the script to a shortcut inside your IDE so you can run it as often as you write some ___fy___ code that needs to be processed.
