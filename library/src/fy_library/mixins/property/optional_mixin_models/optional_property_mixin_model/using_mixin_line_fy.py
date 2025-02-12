# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import PropertyMixinModel


property optional_property_mixin_model: PropertyMixinModel | None using mixin_line:
    property mixin_line
fy"""

import abc
import re
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PROPERTY_CONSTANT_IMPLEMENTATION_NAME,
    PROPERTY_SETTER_IMPLEMENTATION_NAME,
)
from fy_library.domain.mixin_models import MixinModelKind, PropertyMixinModel
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.optional_mixin_models.optional_property_mixin_model.abc_fy import (
    OptionalPropertyMixinModel_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsing_mixin_model.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)

_FLOW_PROPERTY_REGEX: Final = re.compile(
    rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>(?!constant\b){FY_ENTITY_REGEX_STRING})?"
    rf"(?:\[(?P<generics_impl>{PYTHON_MULTI_ENTITY_REGEX_STRING})])?"
    rf"(?:constant(?:\[(?P<constant_generics_impl>{PYTHON_MULTI_ENTITY_REGEX_STRING})])?\((?P<constant_value>.*)\))?"
    r"\s*$"
)


# fy:start ===>>>
class OptionalPropertyMixinModel_UsingMixinLine_PropertyMixin(
    # Property Mixins
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
        maybe_constant_value = flow_property_fy_search.group("constant_value")
        maybe_implementation_name = flow_property_fy_search.group("implementation_name")

        assert maybe_implementation_name is not None or maybe_constant_value is not None

        python_class_implementation_name = PythonEntityName.from_snake_case(
            flow_property_fy_search.group("implementation_name")
            or PROPERTY_SETTER_IMPLEMENTATION_NAME
        )

        python_class_name = PythonEntityName.from_pascal_case(
            f"{ property_name.pascal_case }_Using{ python_class_implementation_name.pascal_case }_PropertyMixin"
        )

        implementation_name: PythonEntityName = PythonEntityName.from_snake_case(
            flow_property_fy_search.group("implementation_name")
            or PROPERTY_CONSTANT_IMPLEMENTATION_NAME
        )

        assert (
            flow_property_fy_search.group("generics_impl") is None
            or flow_property_fy_search.group("constant_generics_impl") is None
        )

        generics_impl = (
            flow_property_fy_search.group("generics_impl")
            if implementation_name.snake_case != PROPERTY_CONSTANT_IMPLEMENTATION_NAME
            else flow_property_fy_search.group("constant_generics_impl")
        )

        return PropertyMixinModel(
            python_class_name=python_class_name,
            kind=MixinModelKind.PROPERTY,
            property_name=property_name,
            implementation_name=implementation_name,
            generics_impl=generics_impl or "",
            constant_value=flow_property_fy_search.group("constant_value") or "",
            property_type="",
        )
