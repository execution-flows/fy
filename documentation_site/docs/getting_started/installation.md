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
poetry env use 3.10
poetry install
```
### 3. Run the local.fy.sh Script
```bash
./local.fy.sh <path to folder you want to transform>
```
==Note:== The local.fy.sh script is configured with /library/src as the project root folder. Only files within this folder can be processed.

!!! info "Keep Local fy CLI Up to Date"
    Regularly update the local-fy-cli repository to ensure it remains in sync with the primary development fy repo:

    ```bash
    Copy code
    cd local-fy-cli
    git pull origin main
    ```
