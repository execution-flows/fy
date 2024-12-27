# fy:start ===>>>
from typing import Dict


class AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin:
    @property
    def _abstract_entities_ordering_index(self) -> Dict[str, int]:
        return self.__abstract_entities_ordering_index

    @_abstract_entities_ordering_index.setter
    def _abstract_entities_ordering_index(
        self, abstract_entities_ordering_index: Dict[str, int]
    ) -> None:
        self.__abstract_entities_ordering_index = abstract_entities_ordering_index


# fy:end <<<===
