# fy:start ===>>>
from typing import Dict


class OrderedAbstractEntities_UsingSetter_PropertyMixin:
    @property
    def _ordered_abstract_entities(self) -> Dict[str, int]:
        return self.__ordered_abstract_entities

    @_ordered_abstract_entities.setter
    def _ordered_abstract_entities(
        self, ordered_abstract_entities: Dict[str, int]
    ) -> None:
        self.__ordered_abstract_entities = ordered_abstract_entities
        # fy:end <<<===
