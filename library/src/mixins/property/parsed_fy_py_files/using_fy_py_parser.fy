from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile
from flows.parse_fy_py_file import ParseFyPyFile_Flow


property parsed_fy_py_files using fy_py_parser:
    with property fy_py_files_to_parse

    @cached
    def -> List[ParsedFyPyFile]:
        return [
            ParseFyPyFile_Flow(fy_py_file_to_parse=fy_py_file)()
            for fy_py_file in self._fy_py_files_to_parse
        ]
