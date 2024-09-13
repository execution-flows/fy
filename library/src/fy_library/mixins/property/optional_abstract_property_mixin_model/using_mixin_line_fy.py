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

from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.mixin_models import MixinModelKind, AbstractPropertyModel
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)

_ABSTRACT_PROPERTY_MIXIN_REGEX: Final = re.compile(
    rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})$"
)


# fy:start ===>>>
class OptionalAbstractPropertyMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_abstract_property_mixin_model(self) -> AbstractPropertyModel | None:
        # fy:end <<<===
        declared_abstract_property_mixin = _ABSTRACT_PROPERTY_MIXIN_REGEX.search(
            self._mixin_line
        )

        return (
            AbstractPropertyModel(
                kind=MixinModelKind.ABSTRACT_PROPERTY,
                property_name=PythonEntityName.from_snake_case(
                    declared_abstract_property_mixin.group("abstract_property_name")
                ),
            )
            if declared_abstract_property_mixin is not None
            else None
        )
