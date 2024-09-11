# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import BaseMixinModel


property mixin_models: List[BaseMixinModel]
"""

import abc
from typing import List

from fy_library.domain.mixin_models import BaseMixinModel


# fy:start ===>>>
class MixinModels_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_models(self) -> List[BaseMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
