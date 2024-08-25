from base.execution_flow_base import ExecutionFlowBase

from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_parts.using_fy_file_to_parse_docstring_fy import (
    FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin,
)
from mixins.property.fy_code.fy_py_file_parts_fy import (
    FyCode_UsingFyPyFileParts_PropertyMixin,
)
from mixins.property.post_marker_file_content.fy_py_file_parts_fy import (
    PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
)
from mixins.property.pre_marker_file_content.fy_py_file_parts_fy import (
    PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
)
from mixins.property.fy_file_kind.using_fy_code_fy import (
    FyFileKind_UsingFyCode_PropertyMixin,
)
from mixins.method.parse_fy_py_file.using_fy_file_kind__and__fy_code_fy import (
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
)

from pathlib import Path
from typing import Any

from domain.parsed_fy_py_file import ParsedFyPyFile


class ParseFyPyFile_Flow(
    # Property Mixins
    FyPyFileToParse_UsingSetter_PropertyMixin,
    FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin,
    FyCode_UsingFyPyFileParts_PropertyMixin,
    PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
    PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
    FyFileKind_UsingFyCode_PropertyMixin,
    # Method Mixins
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
    # Base
    ExecutionFlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        return self._parse_fy_py_file()

    def __init__(
        self,
        *args: Any,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)
