"""fy
flow HelloWorld -> None:
"""

from base.execution_flow_base import ExecutionFlowBase


# fy:start <<<===
class Helloworld_Flow(
    # Base
    ExecutionFlowBase[None]
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
