"""fy
from domain.fy_py_template_models import AbstractMethodModel
from typing import List


property method_mixins: List[AbstractMethodModel] using mixin_lines:
    property mixin_lines
"""

import abc
import re
from functools import cached_property
from typing import List

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import AbstractMethodModel
from domain.python_entity_name import PythonEntityName
from mixins.property.mixin_lines.abc_fy import (
    With_MixinLines_PropertyMixin_ABC,
)


# fy:start ===>>>
class MethodMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_mixins(self) -> List[AbstractMethodModel]:
        # fy:end <<<===
        abstract_method_mixin_regex = re.compile(
            rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_methods: List[AbstractMethodModel] = []

        for mixin_line in self._mixin_lines.split("\n"):
            if mixin_line.strip() == "":
                continue

            declared_abstract_method_mixin = abstract_method_mixin_regex.search(
                mixin_line
            )

            if declared_abstract_method_mixin is not None:
                abstract_methods.append(
                    AbstractMethodModel(
                        method_name=PythonEntityName.from_snake_case(
                            declared_abstract_method_mixin.group("abstract_method_name")
                        )
                    )
                )

        return abstract_methods
