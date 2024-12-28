# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind


property fy_file_kind: ParsedFyPyFileKind using fy_code:
    property fy_py_file_to_parse
    property fy_code
"""

import abc
import re
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_file_kind.abc_fy import (
    FyFileKind_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)

_FLOW_MATCH_REGEX: Final = re.compile(
    rf"^flow\s+{FY_ENTITY_REGEX_STRING}\s*(\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?\s*"
    rf"(\({FY_ENTITY_REGEX_STRING}\))?\s*"
    rf"(->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*)?:\s*$",
)
_BASE_FLOW_MATCH_REGEX: Final = re.compile(
    rf"^base\s+flow\s+{FY_ENTITY_REGEX_STRING}\s*(\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?\s*"
    rf"(\({FY_ENTITY_REGEX_STRING}\))?\s*"
    rf"->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*$",
)
_METHOD_MATCH_REGEX: Final = re.compile(
    rf"^method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s*"
    rf"(\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?"
    rf"(?P<arguments>\(({PYTHON_ARGUMENTS_REGEX_STRING})\))?\s+->"
    rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*$"
)
_ABSTRACT_METHOD_REGEX: Final = re.compile(
    rf"^method\s+{FY_ENTITY_REGEX_STRING}\s*(\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?(\({PYTHON_ARGUMENTS_REGEX_STRING}\))?"
    rf"\s*|->\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
)
_ABSTRACT_PROPERTY_REGEX: Final = re.compile(
    rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*(\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?:\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
)
_PROPERTY_REGEX: Final = re.compile(
    rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*((\[{PYTHON_MULTI_ENTITY_REGEX_STRING}])?:\s*({PYTHON_MULTI_ENTITY_REGEX_STRING}))\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
)


# fy:start ===>>>
class FyFileKind_UsingFyCode_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    FyFileKind_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        # fy:end <<<===
        for fy_code_line in self._fy_code.split("\n"):
            if _FLOW_MATCH_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.FLOW
            if _BASE_FLOW_MATCH_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.BASE_FLOW
            if _METHOD_MATCH_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.METHOD
            if _ABSTRACT_METHOD_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.ABSTRACT_METHOD
            if _ABSTRACT_PROPERTY_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.ABSTRACT_PROPERTY
            if _PROPERTY_REGEX.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.PROPERTY

        raise ValueError(f"Undetected file type for {self._fy_py_file_to_parse}")
