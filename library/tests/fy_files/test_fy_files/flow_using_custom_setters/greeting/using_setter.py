class Greeting_UsingSetter_PropertyMixin:
    @property
    def _greeting(self) -> str:
        return self.__greeting

    # Hello custom setter
    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
