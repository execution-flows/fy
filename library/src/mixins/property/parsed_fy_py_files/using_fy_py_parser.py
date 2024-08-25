from functools import cached_property

import abc

from mixins.property.fy_py_files_to_parse.abc_fy import (
    With_FyPyFilesToParse_PropertyMixin_ABC,
)

from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile
from flows.parse_fy_py_file import ParseFyPyFile_Flow


class ParsedFyPyFiles_UsingFyPyParser_PropertyMixin(
    # Property_mixins
    With_FyPyFilesToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        return [
            ParseFyPyFile_Flow(fy_py_file_to_parse=fy_py_file)()
            for fy_py_file in self._fy_py_files_to_parse
        ]
