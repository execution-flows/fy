# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property mixin_import_map: Dict[str, str]
"""

from typing import Dict
import abc


# fy:start ===>>>
class MixinImportMap_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_import_map(self) -> Dict[str, str]:
        raise NotImplementedError()
        # fy:end <<<===
