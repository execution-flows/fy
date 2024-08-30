"""fy
from mixins.property.abstract_property_file_split.abc_fy import AbstractPropertyFileSplitModel


property abstract_property_file_split: AbstractPropertyFileSplitModel using abstract_property_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from mixins.property.abstract_property_file_split.abc_fy import (
    AbstractPropertyFileSplitModel,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_property_file_split(self) -> AbstractPropertyFileSplitModel:
        # fy:end <<<===
        abstract_property_regex = re.compile(
            rf"property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*:\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )

        abstract_property_file_split = abstract_property_regex.split(self._fy_code)

        assert (
            len(abstract_property_file_split) == 4
        ), f"Abstract property file split length {len(abstract_property_file_split)} is invalid"

        abstract_property_file_split_model = AbstractPropertyFileSplitModel(
            user_imports=abstract_property_file_split[0],
            abstract_property_name=abstract_property_file_split[1],
            property_type=abstract_property_file_split[2],
        )

        return abstract_property_file_split_model
