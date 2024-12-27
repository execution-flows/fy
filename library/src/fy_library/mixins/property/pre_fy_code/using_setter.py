# fy:start ===>>>
class PreFyCode_UsingSetter_PropertyMixin:
    @property
    def _pre_fy_code(self) -> str:
        return self.__pre_fy_code

    @_pre_fy_code.setter
    def _pre_fy_code(self, pre_fy_code: str) -> None:
        self.__pre_fy_code = pre_fy_code


# fy:end <<<===
