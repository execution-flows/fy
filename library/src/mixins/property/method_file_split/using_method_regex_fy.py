"""fy
from typing import List


property method_file_split: List[str] using method_regex:
    property fy_code
"""

import re
from typing import List

from constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
)


from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
import abc


from functools import cached_property


# fy:start <<<===
class MethodFileSplit_UsingMethodRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_file_split(self) -> List[str]:
        # fy:end <<<===
        method_string_split_regex = re.compile(
            rf"method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s*"
            rf"(?P<arguments>\(({PYTHON_ARGUMENTS_REGEX_STRING})\))?\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        )
        method_file_split = method_string_split_regex.split(self._fy_code)

        assert (
            len(method_file_split)
        ) == 7, f"Method file split length {len(method_file_split)} is invalid."

        return method_file_split
