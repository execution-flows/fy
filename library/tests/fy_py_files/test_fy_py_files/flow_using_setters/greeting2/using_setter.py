# fy:start ===>>>
class Greeting2_UsingSetter_PropertyMixin:
    @property
    def _greeting2(self) -> str:
        return self.__greeting2

    @_greeting2.setter
    def _greeting2(self, greeting2: str) -> None:
        self.__greeting2 = greeting2
        # fy:end <<<===
