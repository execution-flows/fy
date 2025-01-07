# fy:start ===>>>
from fy_library.mixins.property.imports_and_user_imports.cached_import.abc_fy import (
    CachedImport_PropertyMixin_ABC,
)
from typing import List


class CachedImport_UsingSetter_PropertyMixin(
    CachedImport_PropertyMixin_ABC,
):
    @property
    def _cached_import(self) -> List[str]:
        return self.__cached_import

    @_cached_import.setter
    def _cached_import(self, cached_import: List[str]) -> None:
        self.__cached_import = cached_import


# fy:end <<<===
