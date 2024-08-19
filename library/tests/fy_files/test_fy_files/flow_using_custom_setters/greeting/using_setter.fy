property greeting using setter:
    def -> str:
        return self.__greeting

    # Hello custom setter
    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
