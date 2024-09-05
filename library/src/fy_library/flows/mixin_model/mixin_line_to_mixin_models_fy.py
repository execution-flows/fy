# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow MixinLineToMixinModels -> BaseMixinModel:
    property mixin_line using setter
    property fy_py_file_to_parse using setter
"""

import re
from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.fy_py_template_models import BaseMixinModel
from fy_library.domain.fy_py_template_models import (
    MixinModelKind,
    MethodMixinModel,
    AbstractMethodModel,
    AbstractPropertyModel,
    PropertyMixinModel,
)
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mixin_line.using_setter import (
    MixinLine_UsingSetter_PropertyMixin,
)

_FLOW_METHOD_REGEX = re.compile(
    rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)

_FLOW_PROPERTY_REGEX = re.compile(
    rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)

_ABSTRACT_PROPERTY_MIXIN_REGEX = re.compile(
    rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})$"
)

_ABSTRACT_METHOD_MIXIN_REGEX = re.compile(
    rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})$"
)


# fy:start ===>>>
class MixinLineToMixinModels_Flow(
    # Property Mixins
    MixinLine_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    # Base
    FlowBase[BaseMixinModel],
):
    def __init__(
        self,
        *args: Any,
        mixin_line: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._mixin_line = mixin_line
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> BaseMixinModel:
        # fy:end <<<===
        flow_property_fy_search = _FLOW_PROPERTY_REGEX.search(self._mixin_line)

        if flow_property_fy_search is not None:
            return PropertyMixinModel(
                kind=MixinModelKind.PROPERTY,
                property_name=PythonEntityName.from_snake_case(
                    flow_property_fy_search.group("property_name")
                ),
                implementation_name=PythonEntityName.from_snake_case(
                    flow_property_fy_search.group("implementation_name")
                ),
            )

        declared_abstract_property_mixin = _ABSTRACT_PROPERTY_MIXIN_REGEX.search(
            self._mixin_line
        )

        if declared_abstract_property_mixin is not None:
            return AbstractPropertyModel(
                kind=MixinModelKind.ABSTRACT_PROPERTY,
                property_name=PythonEntityName.from_snake_case(
                    declared_abstract_property_mixin.group("abstract_property_name")
                ),
            )

        declared_abstract_method_mixin = _ABSTRACT_METHOD_MIXIN_REGEX.search(
            self._mixin_line
        )

        if declared_abstract_method_mixin is not None:
            return AbstractMethodModel(
                kind=MixinModelKind.ABSTRACT_METHOD,
                method_name=PythonEntityName.from_snake_case(
                    declared_abstract_method_mixin.group("abstract_method_name")
                ),
            )

        flow_method_fy_search = _FLOW_METHOD_REGEX.search(self._mixin_line)

        if flow_method_fy_search is not None:
            return MethodMixinModel(
                kind=MixinModelKind.METHOD,
                method_name=PythonEntityName.from_snake_case(
                    flow_method_fy_search.group("method_name")
                ),
                implementation_name=PythonEntityName.from_snake_case(
                    flow_method_fy_search.group("implementation_name")
                ),
            )

        raise ValueError(
            f"Line {self._mixin_line} in {self._fy_py_file_to_parse} is invalid."
        )
