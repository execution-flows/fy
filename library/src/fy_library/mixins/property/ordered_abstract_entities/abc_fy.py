# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property ordered_abstract_entities: Dict[str, int]
"""

import abc

from typing import Dict


# fy:start ===>>>
class OrderedAbstractEntities_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _ordered_abstract_entities(self) -> Dict[str, int]:
        raise NotImplementedError()
        # fy:end <<<===
