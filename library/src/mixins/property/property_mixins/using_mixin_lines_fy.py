"""fy
from domain.fy_py_template_models import AbstractPropertyModel
from typing import List


property property_mixins: List[AbstractPropertyModel] using mixin_lines:
    with property property_file_split
"""

import re

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import AbstractPropertyModel
from domain.python_entity_name import PythonEntityName
from mixins.property.property_file_split.abc_fy import (
    With_PropertyFileSplit_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start <<<===
class PropertyMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _property_mixins(self) -> List[AbstractPropertyModel]:
        # fy:end <<<===
        abstract_property_mixin_regex = re.compile(
            rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_properties: List[AbstractPropertyModel] = []

        for mixin_line in self._property_file_split[5].split("\n"):
            if mixin_line.strip() == "":
                continue

            declared_abstract_property_mixin = abstract_property_mixin_regex.search(
                mixin_line
            )

            if declared_abstract_property_mixin is not None:
                abstract_properties.append(
                    AbstractPropertyModel(
                        property_name=PythonEntityName.from_snake_case(
                            declared_abstract_property_mixin.group(
                                "abstract_property_name"
                            )
                        )
                    )
                )

        return abstract_properties
