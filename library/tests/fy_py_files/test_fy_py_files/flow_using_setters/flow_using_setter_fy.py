"""fy
flow SetterTest -> None:
    property greeting using setter
"""

from base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.flow_using_setters.greeting.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)


# fy:start <<<===
class SetterTest_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
