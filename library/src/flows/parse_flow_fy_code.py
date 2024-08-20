from base.execution_flow_base import ExecutionFlowBase

from mixins.property.fy_code.using_setter import FyCode_UsingSetter_PropertyMixin

from domain.parsed_fy_py_file import ParsedFyPyFile
from typing import Any


class ParseFlowFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    # Base
    ExecutionFlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        return ParsedFyPyFile()

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        super().__init__(*args, **kwargs)
