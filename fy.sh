#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
FY_CLI_DIR="${SCRIPT_DIR}/cli"

pushd "${FY_CLI_DIR}" >> /dev/null || exit 1

poetry run fy --root "$CURRENT_DIR" "$CURRENT_DIR"

EXIT_CODE=$?

popd || exit 1

exit $EXIT_CODE
