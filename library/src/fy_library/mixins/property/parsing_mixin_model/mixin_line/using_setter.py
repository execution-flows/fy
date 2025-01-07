# fy:start ===>>>
from fy_library.mixins.property.parsing_mixin_model.mixin_line.abc_fy import (
    MixinLine_PropertyMixin_ABC,
)


class MixinLine_UsingSetter_PropertyMixin(
    MixinLine_PropertyMixin_ABC,
):
    @property
    def _mixin_line(self) -> str:
        return self.__mixin_line

    @_mixin_line.setter
    def _mixin_line(self, mixin_line: str) -> None:
        self.__mixin_line = mixin_line


# fy:end <<<===
