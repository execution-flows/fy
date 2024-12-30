# fy:start ===>>>
from typing import List


class CachedImport_UsingSetter_PropertyMixin:
    @property
    def _cached_import(self) -> List[str]:
        return self.__cached_import

    @_cached_import.setter
    def _cached_import(self, cached_import: List[str]) -> None:
        self.__cached_import = cached_import


# fy:end <<<===
