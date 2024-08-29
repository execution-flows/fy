"""fy
property property_file_split: PropertyFileSplit using property_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from domain.python_entity_name import PythonEntityName
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.property_file_split.abc_fy import PropertyFileSplitModel


# fy:start ===>>>
class PropertyFileSplit_UsingPropertyRegex_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_file_split(self) -> PropertyFileSplitModel:
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

        property_name = PythonEntityName.from_snake_case(property_file_split[2])
        implementation_name = PythonEntityName.from_snake_case(property_file_split[4])
        property_file_split_model = PropertyFileSplitModel(
            user_imports=property_file_split[0],
            python_class_name=PythonEntityName.from_pascal_case(
                f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
            ),
            property_name=property_name,
            implementation_name=implementation_name,
            property_type=property_file_split[3],
            mixin_split=property_file_split[5].split("\n"),
        )

        return property_file_split_model
