# fy:start ===>>>
from fy_py_files.test_fy_py_files.hello_world_using_property.property.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from pathlib import Path


class Greeting_UsingSetter_PropertyMixin(
    Greeting_PropertyMixin_ABC,
):
    @property
    def _greeting(self) -> Path:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: Path) -> None:
        self.__greeting = greeting


# fy:end <<<===
