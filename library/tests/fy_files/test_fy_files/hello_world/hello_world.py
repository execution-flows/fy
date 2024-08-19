from base.execution_flow_base import ExecutionFlowBase

from datetime import datetime


class HelloWorld_Flow(
    # Base
    ExecutionFlowBase[None]
):
    def __call__(self) -> None:
        datetime.now()
        print("Hello world!")
