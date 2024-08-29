"""fy
from domain.fy_py_template_models import MethodMixinModel
from typing import List


property method_mixins: List[MethodMixinModel] using flow_mixin_lines:
    property mixin_lines
"""

import re

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import MethodMixinModel
from functools import cached_property

from domain.python_entity_name import PythonEntityName
from mixins.property.mixin_lines.abc_fy import (
    With_MixinLines_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start ===>>>
class MethodMixins_UsingFlowMixinLines_PropertyMixin(
    # Property_mixins
    With_MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_mixins(self) -> List[MethodMixinModel]:
        # fy:end <<<===
        flow_method_regex = re.compile(
            rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )

        methods: List[MethodMixinModel] = []

        for mixin_line in self._mixin_lines:
            if mixin_line.strip() == "":
                continue

            flow_method_fy_search = flow_method_regex.search(mixin_line)

            if flow_method_fy_search:
                methods.append(
                    MethodMixinModel(
                        method_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("method_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("implementation_name")
                        ),
                    )
                )

        return methods
