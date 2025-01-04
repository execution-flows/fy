# fy:start ===>>>
from fy_py_files.test_fy_py_files.flow_using_setters.greeting2.abc_fy import (
    Greeting2_PropertyMixin_ABC,
)


class Greeting2_UsingSetter_PropertyMixin(
    Greeting2_PropertyMixin_ABC,
):
    @property
    def _greeting2(self) -> str:
        return self.__greeting2

    @_greeting2.setter
    def _greeting2(self, greeting2: str) -> None:
        self.__greeting2 = greeting2


# fy:end <<<===
