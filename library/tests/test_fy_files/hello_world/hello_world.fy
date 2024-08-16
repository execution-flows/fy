from datetime import datetime

flow HelloWorld:
    def -> None:
        datetime.now()
        print("Hello world!")
