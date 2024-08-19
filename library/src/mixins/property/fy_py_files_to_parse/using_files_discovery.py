from functools import cached_property

import abc

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
        fy_py_files_in_directory = list(self._folder_to_parse.rglob("*.fy.py"))
        fy_py_files: List[Path] = []

        for fy_py_file in fy_py_files_in_directory:
            with open(file=fy_py_file, mode="r") as file:
                first_six_bytes = file.read(6)
                if first_six_bytes == '"""fy\n':
                    fy_py_files.append(fy_py_file)
                else:
                    raise SyntaxError(f"File {fy_py_file} doesn't obey Fy syntax")
        return fy_py_files
