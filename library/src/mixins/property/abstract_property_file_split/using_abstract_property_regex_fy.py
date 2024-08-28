"""fy
from typing import List


property abstract_property_file_split: List[str] using abstract_property_regex:
    property fy_code
"""

import re
from typing import List

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
import abc


from functools import cached_property


# fy:start <<<===
class AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_property_file_split(self) -> List[str]:
        # fy:end <<<===
        abstract_property_regex = re.compile(
            rf"property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*:\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )

        abstract_property_file_split = abstract_property_regex.split(self._fy_code)

        assert (
            len(abstract_property_file_split) == 4
        ), f"Abstract property file split length {len(abstract_property_file_split)} is invalid"

        return abstract_property_file_split
