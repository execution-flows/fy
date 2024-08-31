# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import re

FY_PY_FILE_SIGNATURE = '"""fy\n'

FY_CODE_FILE_END_SIGNATURE = '"""'

FY_ENTITY_REGEX_STRING = r"\w+"

PYTHON_ARGUMENTS_REGEX_STRING = r"\s*[^)]*\s*"

PYTHON_ENTITY_CHAR_REGEX_STRING = r"[\w.\[\]]"

PYTHON_MULTI_ENTITY_REGEX_STRING = (
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}|"
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}[\w.\[\]\s\|\,]*{PYTHON_ENTITY_CHAR_REGEX_STRING}"
)

FY_START_MARKER = "# fy:start ===>>>"

FY_END_MARKER = f"{' '*8}# fy:end <<<==="

FY_PY_FILE_EXTENSION = "_fy.py"

NEW_LINE = "\n"

IMPORT_REGEX = re.compile(
    r"^(?P<from>from [\w.]+) import .*$|^(?P<import>import [\w.]+)$", flags=re.DOTALL
)
