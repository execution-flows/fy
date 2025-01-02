# fy:start ===>>>
class FyCode_UsingSetter_PropertyMixin:
    @property
    def _fy_code(self) -> str:
        return self.__fy_code

    @_fy_code.setter
    def _fy_code(self, fy_code: str) -> None:
        self.__fy_code = fy_code


# fy:end <<<===
