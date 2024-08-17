from typing import Dict

from domain.parsed_fy_file import ParsedFyFile


property parse_fy_files_map_by_key using parsed_fy_files:
    with property parsed_fy_files

    @cached
    def -> Dict[str, ParsedFyFile]:
        return {
            parsed_fy_file.template_model.mixin_key: parsed_fy_file
            for parsed_fy_file in self._parsed_fy_files
        }
