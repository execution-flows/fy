# fy:start ===>>>
from typing import List


class MixinImports_UsingSetter_PropertyMixin:
    @property
    def _mixin_imports(self) -> List[str]:
        return self.__mixin_imports

    @_mixin_imports.setter
    def _mixin_imports(self, mixin_imports: List[str]) -> None:
        self.__mixin_imports = mixin_imports
        # fy:end <<<===
