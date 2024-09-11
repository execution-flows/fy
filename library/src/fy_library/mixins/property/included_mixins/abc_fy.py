# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property included_mixins: IncludedMixinsModel
"""

import abc
from typing import List

from pydantic import BaseModel

from fy_library.domain.mixin_models import (
    MethodMixinModel,
    AbstractMethodModel,
    AbstractPropertyModel,
    PropertyMixinModel,
)


class IncludedMixinsModel(BaseModel):
    abstract_method_mixins: List[AbstractMethodModel]
    abstract_property_mixins: List[AbstractPropertyModel]
    method_mixins: List[MethodMixinModel]
    property_mixins: List[PropertyMixinModel]


# fy:start ===>>>
class IncludedMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _included_mixins(self) -> IncludedMixinsModel:
        raise NotImplementedError()
        # fy:end <<<===
