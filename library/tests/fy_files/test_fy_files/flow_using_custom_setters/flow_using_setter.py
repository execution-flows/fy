from base.execution_flow_base import ExecutionFlowBase

from fy_files.test_fy_files.flow_using_custom_setters.greeting.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)


class SetterTest_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        print(self._greeting)
