import abc
import os
from typing import List

from domain.parsed_fy_file import ParsedFyFile
from mixins.property.fy_files_to_parse.abc import With_FyFilesToParse_PropertyMixin_ABC
from parser.fy_file_parser import FyFileParser


class ParsedFyFiles_UsingFyParser_PropertyMixin(
    With_FyFilesToParse_PropertyMixin_ABC,
    abc.ABC
):
    @property
    def _parsed_fy_files(self) -> List[ParsedFyFile]:
        return [
            FyFileParser.parse(fy_file_path)
            for fy_file_path in self._fy_files_to_parse
        ]
