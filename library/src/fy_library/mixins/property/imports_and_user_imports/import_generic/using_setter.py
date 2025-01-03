# fy:start ===>>>
from typing import List


class ImportGeneric_UsingSetter_PropertyMixin:
    @property
    def _import_generic(self) -> List[str]:
        return self.__import_generic

    @_import_generic.setter
    def _import_generic(self, import_generic: List[str]) -> None:
        self.__import_generic = import_generic


# fy:end <<<===
