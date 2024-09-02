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

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyFileKind_UsingFyCode_PropertyMixin(
    # Property_mixins
    FyPyFileToParse_PropertyMixin_ABC,
    FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        # fy:end <<<===
        flow_match_regex = re.compile(
            rf"^flow\s+{FY_ENTITY_REGEX_STRING}(\s+extends\s+{FY_ENTITY_REGEX_STRING})?\s*"
            rf"->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*$",
        )
        method_match_regex = re.compile(
            rf"^method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s*"
            rf"(?P<arguments>\(({PYTHON_ARGUMENTS_REGEX_STRING})\))?\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*$"
        )
        abstract_method_regex = re.compile(
            rf"^method\s+{FY_ENTITY_REGEX_STRING}\s*(\({PYTHON_ARGUMENTS_REGEX_STRING}\))?"
            rf"\s*->\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )
        abstract_property_regex = re.compile(
            rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*:\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )
        property_regex = re.compile(
            rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*:\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
        )

        for fy_code_line in self._fy_code.split("\n"):
            if flow_match_regex.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.FLOW
            if method_match_regex.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.METHOD
            if abstract_method_regex.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.ABSTRACT_METHOD
            if abstract_property_regex.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.ABSTRACT_PROPERTY
            if property_regex.match(fy_code_line) is not None:
                return ParsedFyPyFileKind.PROPERTY

        raise ValueError(f"Undetected file type for {self._fy_py_file_to_parse}")