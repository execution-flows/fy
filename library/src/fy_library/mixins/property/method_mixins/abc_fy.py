# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import MethodMixinModel


property method_mixins: List[MethodMixinModel]
"""

import abc
from typing import List

from fy_library.domain.mixin_models import MethodMixinModel


# fy:start ===>>>
class MethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_mixins(self) -> List[MethodMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
