# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mro_algorithm_models import EntityForLevelDetermination


property entities_for_level_determination: List[EntityForLevelDetermination]
"""

import abc
from typing import List

from fy_library.domain.mro_algorithm_models import EntityForLevelDetermination


# fy:start ===>>>
class EntitiesForLevelDetermination_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _entities_for_level_determination(self) -> List[EntityForLevelDetermination]:
        raise NotImplementedError()
        # fy:end <<<===
