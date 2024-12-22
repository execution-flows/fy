# fy:start ===>>>
from typing import List

from fy_library.domain.mro_algorithm_models import EntityForLevelDetermination


class EntitiesForLevelDetermination_UsingSetter_PropertyMixin:
    @property
    def _entities_for_level_determination(self) -> List[EntityForLevelDetermination]:
        return self.__entities_for_level_determination

    @_entities_for_level_determination.setter
    def _entities_for_level_determination(
        self, entities_for_level_determination: List[EntityForLevelDetermination]
    ) -> None:
        self.__entities_for_level_determination = entities_for_level_determination


# fy:end <<<===
