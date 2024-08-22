from typing import Dict

from domain.parsed_fy_py_file import ParsedFyPyFile


property parse_fy_py_files_map_by_key using parsed_fy_py_files:
    with property parsed_fy_py_files

    @cached
    def -> Dict[str, ParsedFyPyFile]:
        return {
            parsed_fy_py_file.template_model.entity_key: parsed_fy_py_file
            for parsed_fy_py_file in self._parsed_fy_py_files
        }
