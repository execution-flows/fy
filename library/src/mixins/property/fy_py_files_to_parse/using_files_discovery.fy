from pathlib import Path
from typing import List


property fy_py_files_to_parse using files_discovery:
    with property folder_to_parse

    @cached
    def -> List[Path]:
        fy_py_files_in_directory = list(self._folder_to_parse.rglob("*.fy.py"))
        fy_py_files: List[Path] = []

        for fy_py_file in fy_py_files_in_directory:
            with open(file=fy_py_file, mode='r') as file:
                first_six_bytes = file.read(6)
                if first_six_bytes == "\"\"\"fy\n":
                    fy_py_files.append(fy_py_file)
                else:
                    raise SyntaxError(f"File {fy_py_file} doesn't obey Fy syntax")
        return fy_py_files
