# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import AbstractPropertyModel


property optional_abstract_property_mixin_model: AbstractPropertyModel | None using mixin_line:
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
from fy_library.domain.mixin_models import MixinModelKind, AbstractPropertyModel
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)
from fy_library.mixins.property.optional_abstract_property_mixin_model.abc_fy import (
    OptionalAbstractPropertyMixinModel_PropertyMixin_ABC,
)

_ABSTRACT_PROPERTY_MIXIN_REGEX: Final = re.compile(
    rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})(?:\[(?P<generics_impl>{PYTHON_MULTI_ENTITY_REGEX_STRING})])?$"
)


# fy:start ===>>>
class OptionalAbstractPropertyMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    OptionalAbstractPropertyMixinModel_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_abstract_property_mixin_model(self) -> AbstractPropertyModel | None:
        # fy:end <<<===
        declared_abstract_property_mixin = _ABSTRACT_PROPERTY_MIXIN_REGEX.search(
            self._mixin_line
        )
        if declared_abstract_property_mixin is None:
            return None
        property_name = PythonEntityName.from_snake_case(
            declared_abstract_property_mixin.group("abstract_property_name")
        )

        return AbstractPropertyModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{ property_name.pascal_case }_PropertyMixin_ABC"
            ),
            kind=MixinModelKind.ABSTRACT_PROPERTY,
            property_name=property_name,
            generics_impl=declared_abstract_property_mixin.group("generics_impl") or "",
        )
