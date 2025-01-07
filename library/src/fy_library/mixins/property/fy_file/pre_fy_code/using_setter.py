# fy:start ===>>>
from fy_library.mixins.property.fy_file.pre_fy_code.abc_fy import (
    PreFyCode_PropertyMixin_ABC,
)


class PreFyCode_UsingSetter_PropertyMixin(
    PreFyCode_PropertyMixin_ABC,
):
    @property
    def _pre_fy_code(self) -> str:
        return self.__pre_fy_code

    @_pre_fy_code.setter
    def _pre_fy_code(self, pre_fy_code: str) -> None:
        self.__pre_fy_code = pre_fy_code


# fy:end <<<===
