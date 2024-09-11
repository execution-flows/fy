# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import MethodMixinModel


property optional_abstract_method_mixin_model: MethodMixinModel | None
"""

import abc

from fy_library.domain.mixin_models import MethodMixinModel


# fy:start ===>>>
class OptionalAbstractMethodMixinModel_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _optional_abstract_method_mixin_model(self) -> MethodMixinModel | None:
        raise NotImplementedError()
        # fy:end <<<===
