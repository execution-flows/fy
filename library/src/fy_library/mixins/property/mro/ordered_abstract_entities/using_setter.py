# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


class AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin:
    @property
    def _abstract_entities_ordering_index(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], int]:
        return self.__abstract_entities_ordering_index

    @_abstract_entities_ordering_index.setter
    def _abstract_entities_ordering_index(
        self,
        abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int],
    ) -> None:
        self.__abstract_entities_ordering_index = abstract_entities_ordering_index


# fy:end <<<===
