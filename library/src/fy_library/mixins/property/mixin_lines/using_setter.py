# fy:start ===>>>
from typing import List


class MixinLines_UsingSetter_PropertyMixin:
    @property
    def _mixin_lines(self) -> List[str]:
        return self.__mixin_lines

    @_mixin_lines.setter
    def _mixin_lines(self, mixin_lines: List[str]) -> None:
        self.__mixin_lines = mixin_lines
        # fy:end <<<===
