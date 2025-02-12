# fy:start ===>>>
from pathlib import Path


class Greeting_UsingSetter_PropertyMixin:
    @property
    def _greeting(self) -> Path:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: Path) -> None:
        self.__greeting = greeting


# fy:end <<<===
