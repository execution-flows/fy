from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile


property required_property_setters_fy_py using parsed_fy_py_files:
    with property parsed_fy_py_files
    with property parse_fy_py_files_map_by_key

    @cached
    def -> List[ParsedFyPyFile]:
        return []
