# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import abc
import unittest
from typing import Any, Dict, List

from fy_library.domain.mro_algorithm_models import EntityForLevelDetermination
from fy_library.mixins.property.mro_algorithm.entities_for_level_determination.using_setter import (
    EntitiesForLevelDetermination_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mro_algorithm.entity_key_to_level_map.using_entity_for_level_determination_fy import (
    EntityKeyToLevelMap_UsingEntityForLevelDetermination_PropertyMixin,
)


class TestEntityKeyToLevelMap_Flow(
    EntitiesForLevelDetermination_UsingSetter_PropertyMixin,
    EntityKeyToLevelMap_UsingEntityForLevelDetermination_PropertyMixin,
    abc.ABC,
):
    def __init__(
        self,
        *args: Any,
        entities_for_level_determination: List[EntityForLevelDetermination],
        **kwargs: Any,
    ):
        self._entities_for_level_determination = entities_for_level_determination
        super().__init__(*args, **kwargs)

    def __call__(self) -> Dict[str, int]:
        return self._entity_key_to_level_map


class TestEntityKeyToLevelMap(unittest.TestCase):
    def test_entity_key_to_level_map(self):
        entity_level_0_1 = EntityForLevelDetermination(
            entity_key="level0-1",
            mixins=[],
        )
        entity_level_0_2 = EntityForLevelDetermination(
            entity_key="level0-2",
            mixins=[],
        )

        entities_for_level_determination = [
            entity_level_0_1,
            entity_level_0_2,
            EntityForLevelDetermination(
                entity_key="level1-1",
                mixins=[entity_level_0_1],
            ),
            EntityForLevelDetermination(
                entity_key="level1-2",
                mixins=[entity_level_0_2],
            ),
            EntityForLevelDetermination(
                entity_key="level1-3",
                mixins=[entity_level_0_1, entity_level_0_2],
            ),
        ]
        entity_key_to_level_map = TestEntityKeyToLevelMap_Flow(
            entities_for_level_determination=entities_for_level_determination,
        )()
        self.assertEqual(
            entity_key_to_level_map,
            {"level0-1": 0, "level0-2": 0, "level1-1": 1, "level1-2": 1, "level1-3": 1},
        )
