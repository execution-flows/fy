# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import PropertyMixinModel


property optional_property_mixin_model: PropertyMixinModel | None using mixin_line:
    property mixin_line
"""

import abc
import re
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
)
from fy_library.domain.mixin_models import MixinModelKind, PropertyMixinModel
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)
from fy_library.mixins.property.optional_property_mixin_model.abc_fy import (
    OptionalPropertyMixinModel_PropertyMixin_ABC,
)

_FLOW_PROPERTY_REGEX: Final = re.compile(
    rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*"
    rf"(?:\[(?P<generics_impl>{PYTHON_MULTI_ENTITY_REGEX_STRING})])?$"
)


# fy:start ===>>>
class OptionalPropertyMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    OptionalPropertyMixinModel_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_property_mixin_model(self) -> PropertyMixinModel | None:
        # fy:end <<<===
        flow_property_fy_search = _FLOW_PROPERTY_REGEX.search(self._mixin_line)

        if flow_property_fy_search is None:
            return None

        property_name: PythonEntityName = PythonEntityName.from_snake_case(
            flow_property_fy_search.group("property_name")
        )
        implementation_name: PythonEntityName = PythonEntityName.from_snake_case(
            flow_property_fy_search.group("implementation_name")
        )

        return PropertyMixinModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{ property_name.pascal_case }_Using{ implementation_name.pascal_case }_PropertyMixin"
            ),
            kind=MixinModelKind.PROPERTY,
            property_name=property_name,
            implementation_name=implementation_name,
            generics_impl=flow_property_fy_search.group("generics_impl") or "",
        )
