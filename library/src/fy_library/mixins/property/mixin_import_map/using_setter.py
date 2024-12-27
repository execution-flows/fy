# fy:start ===>>>
from typing import Dict


class MixinImportMap_UsingSetter_PropertyMixin:
    @property
    def _mixin_import_map(self) -> Dict[str, str]:
        return self.__mixin_import_map

    @_mixin_import_map.setter
    def _mixin_import_map(self, mixin_import_map: Dict[str, str]) -> None:
        self.__mixin_import_map = mixin_import_map


# fy:end <<<===
