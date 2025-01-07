# fy:start ===>>>
from fy_library.mixins.property.imports_and_user_imports.import_generic.abc_fy import (
    ImportGeneric_PropertyMixin_ABC,
)
from typing import List


class ImportGeneric_UsingSetter_PropertyMixin(
    ImportGeneric_PropertyMixin_ABC,
):
    @property
    def _import_generic(self) -> List[str]:
        return self.__import_generic

    @_import_generic.setter
    def _import_generic(self, import_generic: List[str]) -> None:
        self.__import_generic = import_generic


# fy:end <<<===
