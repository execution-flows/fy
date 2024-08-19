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
        return []
