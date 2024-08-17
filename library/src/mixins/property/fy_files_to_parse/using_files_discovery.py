from functools import cached_property

import abc

from mixins.property.folder_to_parse.abc import With_FolderToParse_PropertyMixin_ABC
from pathlib import Path
from typing import List


class FyFilesToParse_UsingFilesDiscovery_PropertyMixin(
    # Property_mixins
    With_FolderToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_files_to_parse(self) -> List[Path]:
        fy_files_in_directory = list(self._folder_to_parse.rglob("*.fy"))
        return [
            fy_file_path
            for fy_file_path in fy_files_in_directory
            if fy_file_path.is_file()
        ]
