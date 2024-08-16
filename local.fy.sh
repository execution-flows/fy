#!/usr/bin/env bash

# Instructs Bash to exit immediately if any command in the script returns a non-zero exit code.
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
LOCAL_FY_CLI_DIR="${SCRIPT_DIR}/../local-fy-cli/cli"

pushd "${LOCAL_FY_CLI_DIR}" >> /dev/null

poetry run fy --root "${SCRIPT_DIR}/library/src" "$1"

popd
