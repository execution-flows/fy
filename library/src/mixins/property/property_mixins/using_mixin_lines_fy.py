"""fy
from domain.fy_py_template_models import AbstractPropertyModel
from typing import List


property property_mixins: List[AbstractPropertyModel] using mixin_lines:
    property mixin_lines
"""

import abc
import re
from functools import cached_property
from typing import List

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import AbstractPropertyModel
from domain.python_entity_name import PythonEntityName
from mixins.property.mixin_lines.abc_fy import (
    With_MixinLines_PropertyMixin_ABC,
)


# fy:start <<<===
class PropertyMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_mixins(self) -> List[AbstractPropertyModel]:
        # fy:end <<<===
        abstract_property_mixin_regex = re.compile(
            rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_properties: List[AbstractPropertyModel] = []

        for mixin_line in self._mixin_lines:
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
