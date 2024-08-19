flow HelloWorld:
    property greeting using constant

    def -> None:
        print(self._greeting)
