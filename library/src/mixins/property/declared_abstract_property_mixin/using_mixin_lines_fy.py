"""fy
from domain.fy_py_template_models import AbstractPropertyModel
from typing import List


property declared_abstract_property_mixin: List[AbstractPropertyModel] using mixin_lines:
    with property method_file_split
"""

import re
from typing import List

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import AbstractPropertyModel
from domain.python_entity_name import PythonEntityName

from mixins.property.method_file_split.abc_fy import (
    With_MethodFileSplit_PropertyMixin_ABC,
)
import abc


# fy:start <<<===
class DeclaredAbstractPropertyMixin_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_MethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _declared_abstract_property_mixin(self) -> List[AbstractPropertyModel]:
        # fy:end <<<===
        abstract_property_mixin_regex = re.compile(
            rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_properties: List[AbstractPropertyModel] = []

        for mixin_line in self._method_file_split[6].split("\n"):
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
