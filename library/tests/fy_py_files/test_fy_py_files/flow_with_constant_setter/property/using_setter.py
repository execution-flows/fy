# fy:start ===>>>
from fy_py_files.test_fy_py_files.flow_with_constant_setter.property.abc_fy import (
    Greeting_PropertyMixin_ABC,
)


class Greeting_UsingSetter_PropertyMixin(
    Greeting_PropertyMixin_ABC,
):
    @property
    def _greeting(self) -> str:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting


# fy:end <<<===
