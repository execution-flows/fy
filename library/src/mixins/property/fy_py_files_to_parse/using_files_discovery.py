from functools import cached_property

import abc

from constants import FY_PY_FILE_SIGNATURE, FY_PY_FILE_EXTENSION
from mixins.property.folder_to_parse.abc import With_FolderToParse_PropertyMixin_ABC

from pathlib import Path
from typing import List


class FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin(
    # Property_mixins
    With_FolderToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_files_to_parse(self) -> List[Path]:
        fy_py_files_in_directory = list(
            self._folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}")
        )
        fy_py_files: List[Path] = []

        for fy_py_file in fy_py_files_in_directory:
            with open(file=fy_py_file, mode="r") as file:
                current_fy_py_file_signature = file.read(len(FY_PY_FILE_SIGNATURE))
                if current_fy_py_file_signature == FY_PY_FILE_SIGNATURE:
                    fy_py_files.append(fy_py_file)
                else:
                    raise SyntaxError(
                        f"File {fy_py_file} does not start with {FY_PY_FILE_SIGNATURE}"
                    )
        return fy_py_files
