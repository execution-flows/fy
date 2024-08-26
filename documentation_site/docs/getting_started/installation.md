To ensure that the development version of the `fy` tool remains stable, follow these steps to set up a separate local copy for running the `fy` CLI tool.

### 1. Clone the Repo for Local `fy` CLI Tool

Clone the `fy` repository into a separate directory named `local-fy-cli`:

```bash
git clone git@github.com:execution-flows/fy.git local-fy-cli
```
### 2. Set Up Poetry in the Local fy CLI Directory
Navigate to the local-fy-cli/cli directory and set up the Python environment using Poetry:
```bash
cd local-fy-cli/cli
```
!!! info
    The `fy` tool also supports Python 3.11 and 3.12. If you do not have Python 3.10 installed, change `poetry env use` to a version that you have installed.
```bash
poetry env use 3.10
poetry install
```
### 3. Run the local.fy.sh Script
```bash
./fy.sh <path to folder you want to transform>
```

