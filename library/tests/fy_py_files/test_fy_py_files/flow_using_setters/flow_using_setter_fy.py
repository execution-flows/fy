"""fy
flow SetterTest -> None:
    property greeting using setter
    property greeting2 using setter
"""

from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.flow_using_setters.greeting.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)
from fy_py_files.test_fy_py_files.flow_using_setters.greeting2.using_setter import (
    Greeting2_UsingSetter_PropertyMixin,
)
from typing import Any
import datetime


# fy:start ===>>>
class SetterTest_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin,
    Greeting2_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        greeting: datetime.datetime,
        greeting2: str,
        **kwargs: Any,
    ):
        self._greeting = greeting
        self._greeting2 = greeting2
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        pass
