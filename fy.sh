#!/usr/bin/env bash

# Instructs Bash to exit immediately if any command in the script returns a non-zero exit code.
set -e

CURRENT_DIR=$(pwd)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
FY_CLI_DIR="${SCRIPT_DIR}/cli"

pushd "${FY_CLI_DIR}" >> /dev/null

poetry run fy --root "$CURRENT_DIR" "$CURRENT_DIR" | exit

popd
