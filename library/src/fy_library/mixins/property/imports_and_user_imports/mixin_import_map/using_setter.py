# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


class MixinImportMap_UsingSetter_PropertyMixin:
    @property
    def _mixin_import_map(self) -> dict[tuple[ParsedFyPyFileKind, str], str]:
        return self.__mixin_import_map

    @_mixin_import_map.setter
    def _mixin_import_map(
        self, mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str]
    ) -> None:
        self.__mixin_import_map = mixin_import_map


# fy:end <<<===
