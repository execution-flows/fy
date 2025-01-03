# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_flow_base: List[str]
fy"""

from typing import List

import abc


# fy:start ===>>>
class ImportFlowBase_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _import_flow_base(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
