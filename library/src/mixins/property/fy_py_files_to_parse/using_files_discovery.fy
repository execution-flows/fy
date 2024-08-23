from pathlib import Path
from typing import List
from constants import FY_PY_FILE_SIGNATURE, FY_PY_FILE_EXTENSION


property fy_py_files_to_parse using files_discovery:
    with property folder_to_parse

    @cached
    def -> List[Path]:
        fy_py_files_in_directory = list(self._folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}"))
        fy_py_files: List[Path] = []

        for fy_py_file in fy_py_files_in_directory:
            with open(file=fy_py_file, mode='r') as file:
                current_fy_py_file_signature = file.read(len(FY_PY_FILE_SIGNATURE))
                if current_fy_py_file_signature == FY_PY_FILE_SIGNATURE:
                    fy_py_files.append(fy_py_file)
                else:
                    raise SyntaxError(f"File {fy_py_file} does not start with {FY_PY_FILE_SIGNATURE}")
        return fy_py_files
