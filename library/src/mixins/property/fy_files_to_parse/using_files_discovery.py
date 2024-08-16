# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
from functools import cached_property
from pathlib import Path
from typing import List

from mixins.property.folder_to_parse.abc import With_FolderToParse_PropertyMixin_ABC


class FyFilesToParse_UsingFilesDiscovery_PropertyMixin(
    With_FolderToParse_PropertyMixin_ABC, abc.ABC
):
    @cached_property
    def _fy_files_to_parse(self) -> List[Path]:
        fy_files_in_directory = list(self._folder_to_parse.rglob("*.fy"))
        return [
            fy_file_path
            for fy_file_path in fy_files_in_directory
            if fy_file_path.is_file()
        ]
