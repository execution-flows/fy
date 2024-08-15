flow HelloWorld:
    property greeting using constant
    method greet using greeting

    def -> None:
        self._greet()
