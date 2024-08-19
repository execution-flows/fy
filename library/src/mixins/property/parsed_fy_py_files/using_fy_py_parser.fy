from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile
from parser.fy_py_file_parser import FyPYFileParser


property parsed_fy_py_files using fy_py_parser:
    with property fy_py_files_to_parse

    @cached
    def -> List[ParsedFyPyFile]:
        return []
