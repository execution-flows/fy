from typing import List

property parsed_fy_files using fy_parser:

    @cached
    def -> List[ParsedFyFile]
        return [
            FyFileParser.parse(fy_file_path) for fy_file_path in self._fy_files_to_parse
        ]
