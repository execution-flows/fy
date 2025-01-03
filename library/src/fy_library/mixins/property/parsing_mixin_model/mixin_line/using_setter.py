# fy:start ===>>>
class MixinLine_UsingSetter_PropertyMixin:
    @property
    def _mixin_line(self) -> str:
        return self.__mixin_line

    @_mixin_line.setter
    def _mixin_line(self, mixin_line: str) -> None:
        self.__mixin_line = mixin_line


# fy:end <<<===
