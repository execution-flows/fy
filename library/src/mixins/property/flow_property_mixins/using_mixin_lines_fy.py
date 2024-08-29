"""fy
from domain.fy_py_template_models import PropertyMixinModel
from typing import List


property flow_property_mixins: List[PropertyMixinModel] using mixin_lines:
    property mixin_lines
"""

import abc
import re
from functools import cached_property
from typing import List

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import PropertyMixinModel
from domain.python_entity_name import PythonEntityName
from mixins.property.mixin_lines.abc_fy import (
    With_MixinLines_PropertyMixin_ABC,
)


# fy:start ===>>>
class FlowPropertyMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _flow_property_mixins(self) -> List[PropertyMixinModel]:
        # fy:end <<<===
        flow_property_regex = re.compile(
            rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )

        properties: List[PropertyMixinModel] = []

        for mixin_line in self._mixin_lines.split("\n"):
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
