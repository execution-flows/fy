# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.


FY_PY_FILE_SIGNATURE = '"""fy\n'
FY_CODE_FILE_END_SIGNATURE = '"""'
FY_ENTITY_REGEX_STRING = r"\w+"
PYTHON_ENTITY_CHAR_REGEX_STRING = r"[\w.\[\]]"
PYTHON_MULTI_ENTITY_REGEX_STRING = (
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}|"
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}[\w.\[\]\s\|\,]*{PYTHON_ENTITY_CHAR_REGEX_STRING}"
)
