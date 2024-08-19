from pathlib import Path
from typing import List


property fy_py_files_to_parse using files_discovery:
    with property folder_to_parse

    @cached
    def -> List[Path]:
        fy_py_files_in_directory = list(self._folder_to_parse.rglob("*.fy.py"))
        return [
            fy_py_file_path
            for fy_py_file_path in fy_py_files_in_directory
            if fy_py_file_path.is_file()
        ]
