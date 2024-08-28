"""fy
from domain.fy_py_template_models import AbstractMethodModel
from typing import List


property declared_abstract_method_mixins: List[AbstractMethodModel] using mixin_lines:
    property method_file_split
"""

import re

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import AbstractMethodModel
from typing import List

from domain.python_entity_name import PythonEntityName


from mixins.property.method_file_split.abc_fy import (
    With_MethodFileSplit_PropertyMixin_ABC,
)
import abc


# fy:start <<<===
class DeclaredAbstractMethodMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    With_MethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _declared_abstract_method_mixins(self) -> List[AbstractMethodModel]:
        # fy:end <<<===
        abstract_method_mixin_regex = re.compile(
            rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_methods: List[AbstractMethodModel] = []

        for mixin_line in self._method_file_split[6].split("\n"):
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
