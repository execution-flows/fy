from pathlib import Path
from typing import List

property fy_files_to_parse using files_discovery:

    @cached
    def -> List[Path]
        fy_files_in_directory = list(self._folder_to_parse.rglob("*.fy"))
        return [
            fy_file_path
            for fy_file_path in fy_files_in_directory
            if fy_file_path.is_file()
        ]
