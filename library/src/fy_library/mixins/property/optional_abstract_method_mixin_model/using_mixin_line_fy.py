# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import AbstractMethodModel


property optional_abstract_method_mixin_model: AbstractMethodModel | None using mixin_line:
    property mixin_line
"""

import re
from functools import cached_property

from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.fy_py_template_models import AbstractMethodModel, MixinModelKind
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)
import abc

_ABSTRACT_METHOD_MIXIN_REGEX = re.compile(
    rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})$"
)


# fy:start ===>>>
class OptionalAbstractMethodMixinModel_UsingMixinLine_PropertyMixin(
    # Property_mixins
    MixinLine_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_abstract_method_mixin_model(self) -> AbstractMethodModel | None:
        # fy:end <<<===
        declared_abstract_method_mixin = _ABSTRACT_METHOD_MIXIN_REGEX.search(
            self._mixin_line
        )

        return (
            AbstractMethodModel(
                kind=MixinModelKind.ABSTRACT_METHOD,
                method_name=PythonEntityName.from_snake_case(
                    declared_abstract_method_mixin.group("abstract_method_name")
                ),
            )
            if declared_abstract_method_mixin is not None
            else None
        )
