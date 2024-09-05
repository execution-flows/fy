# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import PropertyMixinModel


property optional_property_mixin_model: PropertyMixinModel | None using mixin_line:
    property mixin_line
"""

import re
from functools import cached_property

from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.fy_py_template_models import PropertyMixinModel, MixinModelKind
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)
import abc

_FLOW_PROPERTY_REGEX = re.compile(
    rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)


# fy:start ===>>>
class OptionalPropertyMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_property_mixin_model(self) -> PropertyMixinModel | None:
        # fy:end <<<===
        flow_property_fy_search = _FLOW_PROPERTY_REGEX.search(self._mixin_line)
        return (
            PropertyMixinModel(
                kind=MixinModelKind.PROPERTY,
                property_name=PythonEntityName.from_snake_case(
                    flow_property_fy_search.group("property_name")
                ),
                implementation_name=PythonEntityName.from_snake_case(
                    flow_property_fy_search.group("implementation_name")
                ),
            )
            if flow_property_fy_search is not None
            else None
        )
