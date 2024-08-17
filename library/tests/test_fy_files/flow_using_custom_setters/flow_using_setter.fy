flow SetterTest:
    property greeting using setter

    def -> None:
        print(self._greeting)
