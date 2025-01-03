# fy:start ===>>>
from typing import List


class ImportAbc_UsingSetter_PropertyMixin:
    @property
    def _import_abc(self) -> List[str]:
        return self.__import_abc

    @_import_abc.setter
    def _import_abc(self, import_abc: List[str]) -> None:
        self.__import_abc = import_abc


# fy:end <<<===
