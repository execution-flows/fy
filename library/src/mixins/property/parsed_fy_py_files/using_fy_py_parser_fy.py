"""fy
from typing import List
from domain.parsed_fy_py_file import ParsedFyPyFile


@cached
property parsed_fy_py_files: List[ParsedFyPyFile] using fy_py_parser:
    property fy_py_files_to_parse
"""

from domain.parsed_fy_py_file import ParsedFyPyFile
from flows.parse_fy_py_file_fy import ParseFyPyFile_Flow
from functools import cached_property
from mixins.property.fy_py_files_to_parse.abc_fy import (
    With_FyPyFilesToParse_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start <<<===
class ParsedFyPyFiles_UsingFyPyParser_PropertyMixin(
    # Property_mixins
    With_FyPyFilesToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        return [
            ParseFyPyFile_Flow(fy_py_file_to_parse=fy_py_file)()
            for fy_py_file in self._fy_py_files_to_parse
        ]
