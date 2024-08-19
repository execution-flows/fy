from typing import Dict

from domain.parsed_fy_py_file import ParsedFyPyFile


property parse_fy_py_files_map_by_key using parsed_fy_py_files:
    with property parsed_fy_py_files

    @cached
    def -> Dict[str, ParsedFyPyFile]:
        return {}
