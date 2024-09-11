# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import AbstractMethodModel


property abstract_method_mixins: List[AbstractMethodModel]
"""

import abc
from typing import List

from fy_library.domain.mixin_models import AbstractMethodModel


# fy:start ===>>>
class AbstractMethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_method_mixins(self) -> List[AbstractMethodModel]:
        raise NotImplementedError()
        # fy:end <<<===
