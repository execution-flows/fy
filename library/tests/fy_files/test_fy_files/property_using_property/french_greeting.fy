
property greeting using french_greeting:
    with property french_greeting

    @cached
    def -> str:
        return self._french_greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
