import datetime
from typing import Any


class Greet_UsingTimestampedPythonStr_MethodMixin:
    def _greet(self, message: Any) -> None:
        print(f"{datetime.datetime.now().isoformat()}:{str(message)}")
