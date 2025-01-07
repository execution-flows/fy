# fy:start ===>>>
from fy_library.mixins.property.fy_file.fy_code.abc_fy import FyCode_PropertyMixin_ABC


class FyCode_UsingSetter_PropertyMixin(
    FyCode_PropertyMixin_ABC,
):
    @property
    def _fy_code(self) -> str:
        return self.__fy_code

    @_fy_code.setter
    def _fy_code(self, fy_code: str) -> None:
        self.__fy_code = fy_code


# fy:end <<<===
