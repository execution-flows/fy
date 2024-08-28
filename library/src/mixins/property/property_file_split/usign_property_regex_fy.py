"""fy
from typing import List


property property_file_split: List[str] using property_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property
from typing import List

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)


# fy:start <<<===
class PropertyFileSplit_UsingPropertyRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_file_split(self) -> List[str]:
        # fy:end <<<===
        property_regex = re.compile(
            rf"(?P<property_annotation>@cached)?\s*"
            rf"property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*:\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        )

        property_file_split = property_regex.split(self._fy_code)

        assert (
            len(property_file_split) == 6
        ), f"Property file split length {len(property_file_split)} is invalid"

        return property_file_split
