# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property entity_key_to_level_map: Dict[str, int] using entity_for_level_determination:
    property entities_for_level_determination
"""

import abc
from functools import cached_property
from typing import Dict

from fy_library.domain.mro_algorithm_models import EntityForLevelDetermination
from fy_library.mixins.property.mro_algorithm.entities_for_level_determination.abc_fy import (
    EntitiesForLevelDetermination_PropertyMixin_ABC,
)


# fy:start ===>>>
class EntityKeyToLevelMap_UsingEntityForLevelDetermination_PropertyMixin(
    # Property_mixins
    EntitiesForLevelDetermination_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _entity_key_to_level_map(self) -> Dict[str, int]:
        # fy:end <<<===
        entity_key_to_level_map: Dict[str, int] = {}

        def determine_entity_level(entity: EntityForLevelDetermination):
            if entity.entity_key in entity_key_to_level_map:
                return entity_key_to_level_map[entity.entity_key]

            level = (
                max([determine_entity_level(mixin) for mixin in entity.mixins]) + 1
                if len(entity.mixins) > 0
                else 0
            )

            entity_key_to_level_map[entity.entity_key] = level

            return level

        for entity_for_level_determination in self._entities_for_level_determination:
            determine_entity_level(entity_for_level_determination)

        return entity_key_to_level_map
