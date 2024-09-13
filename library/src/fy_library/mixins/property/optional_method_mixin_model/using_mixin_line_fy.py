# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import MethodMixinModel


property optional_method_mixin_model: MethodMixinModel | None using mixin_line:
    property mixin_line
"""

import re
from functools import cached_property
from typing import Final

from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.mixin_models import MethodMixinModel, MixinModelKind
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)
import abc

_FLOW_METHOD_REGEX: Final = re.compile(
    rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)


# fy:start ===>>>
class OptionalMethodMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_method_mixin_model(self) -> MethodMixinModel | None:
        # fy:end <<<===
        flow_method_fy_search = _FLOW_METHOD_REGEX.search(self._mixin_line)

        return (
            MethodMixinModel(
                kind=MixinModelKind.METHOD,
                method_name=PythonEntityName.from_snake_case(
                    flow_method_fy_search.group("method_name")
                ),
                implementation_name=PythonEntityName.from_snake_case(
                    flow_method_fy_search.group("implementation_name")
                ),
            )
            if flow_method_fy_search is not None
            else None
        )
