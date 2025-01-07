# fy:start ===>>>
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


class MixinImportMap_UsingSetter_PropertyMixin(
    MixinImportMap_PropertyMixin_ABC,
):
    @property
    def _mixin_import_map(self) -> dict[tuple[ParsedFyPyFileKind, str], str]:
        return self.__mixin_import_map

    @_mixin_import_map.setter
    def _mixin_import_map(
        self, mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str]
    ) -> None:
        self.__mixin_import_map = mixin_import_map


# fy:end <<<===
