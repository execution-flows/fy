# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from typing import Final

FY_PY_FILE_SIGNATURE: Final = '"""fy\n'

FY_CODE_FILE_END_SIGNATURE: Final = '"""'

FY_ENTITY_REGEX_STRING: Final = r"\w+"

PYTHON_ARGUMENTS_REGEX_STRING: Final = r"\s*[^)]*\s*"

_PYTHON_ENTITY_CHAR_REGEX_STRING: Final = r"[\w\[\]]"

PYTHON_MULTI_ENTITY_REGEX_STRING: Final = (
    rf"{_PYTHON_ENTITY_CHAR_REGEX_STRING}|"
    rf"{_PYTHON_ENTITY_CHAR_REGEX_STRING}[\w\.\[\]\s\|\,]*{_PYTHON_ENTITY_CHAR_REGEX_STRING}"
)

FY_START_MARKER: Final = "# fy:start ===>>>"

FY_END_MARKER: Final = "# fy:end <<<==="

FY_PY_FILE_EXTENSION: Final = "_fy.py"

PROPERTY_SETTER_IMPLEMENTATION_NAME: Final = "setter"
