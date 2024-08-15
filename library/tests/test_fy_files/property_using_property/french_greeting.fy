property greeting using french_greeting:
    with property french_greeting

    def -> str:
        return self._french_greeting
