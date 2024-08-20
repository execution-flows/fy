from base.execution_flow_base import ExecutionFlowBase

from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.fy_code.using_fy_file_to_parse_docstring import (
    FyCode_UsingFyFileToParseDocstring_PropertyMixin,
)
from mixins.property.fy_file_kind.using_fy_code import (
    FyFileKind_UsingFyCode_PropertyMixin,
)
from mixins.method.parse_fy_py_file.fy_file_kind__and__fy_code import (
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
)


class ParseFyPyFile_Flow(
    # Property Mixins
    FyPyFileToParse_UsingSetter_PropertyMixin,
    FyCode_UsingFyFileToParseDocstring_PropertyMixin,
    FyFileKind_UsingFyCode_PropertyMixin,
    # Method Mixins
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        self._parse_fy_py_file()
