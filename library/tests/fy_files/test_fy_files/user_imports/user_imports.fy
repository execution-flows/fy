import datetime
from typing import Any


method greet using timestamped_python_str:
    def(message: Any) -> None:
        print(f"{datetime.datetime.now().isoformat()}:{str(message)}")
