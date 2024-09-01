# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property mixin_imports: List[str]
"""

from typing import List
import abc


# fy:start ===>>>
class MixinImports_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_imports(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
