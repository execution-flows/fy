"""fy
from pathlib import Path
from typing import List


@cached
property fy_py_files_to_parse: List[Path] using files_discovery:
    property folder_to_parse
"""

import abc
from functools import cached_property
from pathlib import Path
from typing import List

from constants import FY_PY_FILE_SIGNATURE, FY_PY_FILE_EXTENSION

from mixins.property.folder_to_parse.abc_fy import (
    FolderToParse_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin(
    # Property_mixins
    FolderToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_files_to_parse(self) -> List[Path]:
        # fy:end <<<===
        fy_py_files_in_directory = list(
            self._folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}")
        )
        fy_py_files: List[Path] = []

        for fy_py_file in fy_py_files_in_directory:
            with open(file=fy_py_file, mode="r") as file:
                while file_line := file.readline():
                    if file_line[0] != "#":
                        break
                if file_line == FY_PY_FILE_SIGNATURE:
                    fy_py_files.append(fy_py_file)
                else:
                    raise SyntaxError(
                        f"File {fy_py_file} does not start with {FY_PY_FILE_SIGNATURE}"
                    )
        return fy_py_files
