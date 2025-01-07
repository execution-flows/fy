# fy:start ===>>>
from fy_library.mixins.property.imports_and_user_imports.import_abc.abc_fy import (
    ImportAbc_PropertyMixin_ABC,
)
from typing import List


class ImportAbc_UsingSetter_PropertyMixin(
    ImportAbc_PropertyMixin_ABC,
):
    @property
    def _import_abc(self) -> List[str]:
        return self.__import_abc

    @_import_abc.setter
    def _import_abc(self, import_abc: List[str]) -> None:
        self.__import_abc = import_abc


# fy:end <<<===
