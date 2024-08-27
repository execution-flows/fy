"""fy
from typing import List

@cached
property abstract_method_file_split: List[str] using abstract_method_regex:
    with property fy_code
"""

import re
from typing import List

from constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
import abc


from functools import cached_property


# fy:start <<<===
class AbstractMethodFileSplit_UsingAbstractMethodRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_method_file_split(self) -> List[str]:
        # fy:end <<<===
        abstract_method_regex = re.compile(
            rf"method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*(\((?P<arguments>{PYTHON_ARGUMENTS_REGEX_STRING})\))?"
            rf"\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )

        abstract_method_file_split = abstract_method_regex.split(self._fy_code)

        assert (
            len(abstract_method_file_split) == 6
        ), f"Abstract Method file split length {len(abstract_method_file_split)} is invalid"

        return abstract_method_file_split
