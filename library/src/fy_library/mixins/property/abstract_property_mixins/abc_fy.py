# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import AbstractPropertyModel


property abstract_property_mixins: List[AbstractPropertyModel]
"""

import abc
from typing import List

from fy_library.domain.mixin_models import AbstractPropertyModel


# fy:start ===>>>
class AbstractPropertyMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_property_mixins(self) -> List[AbstractPropertyModel]:
        raise NotImplementedError()
        # fy:end <<<===
