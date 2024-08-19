flow SetterTest2:
    property greeting using setter

    def -> None:
        print(self._greeting)
