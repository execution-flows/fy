"""fy
property method_file_split: MethodFileSplitModel using method_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property

from constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.method_file_split.abc_fy import MethodFileSplitModel


# fy:start ===>>>
class MethodFileSplit_UsingMethodRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_file_split(self) -> MethodFileSplitModel:
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

        method_file_split_model = MethodFileSplitModel(
            user_imports=method_file_split[0],
            method_name=method_file_split[1],
            implementation_name=method_file_split[5],
            arguments=method_file_split[3],
            return_type=method_file_split[4],
            mixin_split=method_file_split[6].split("\n"),
        )

        return method_file_split_model
