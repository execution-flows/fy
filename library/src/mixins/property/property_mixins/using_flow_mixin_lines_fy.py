"""fy
from domain.fy_py_template_models import PropertyMixinModel
from typing import List


property property_mixins: List[PropertyMixinModel] using flow_mixin_lines:
    property mixin_lines
"""

import re

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import PropertyMixinModel
from functools import cached_property

from domain.python_entity_name import PythonEntityName
from mixins.property.mixin_lines.abc_fy import (
    With_MixinLines_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start ===>>>
class PropertyMixins_UsingFlowMixinLines_PropertyMixin(
    # Property_mixins
    With_MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_mixins(self) -> List[PropertyMixinModel]:
        # fy:end <<<===
        flow_property_regex = re.compile(
            rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )

        properties: List[PropertyMixinModel] = []

        for mixin_line in self._mixin_lines:
            if mixin_line.strip() == "":
                continue

            flow_property_fy_search = flow_property_regex.search(mixin_line)

            if flow_property_fy_search:
                properties.append(
                    PropertyMixinModel(
                        property_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("property_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("implementation_name")
                        ),
                    )
                )

        return properties
