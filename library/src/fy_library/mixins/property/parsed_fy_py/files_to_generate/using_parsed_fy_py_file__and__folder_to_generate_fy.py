# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property files_to_generate: list[ParsedFyPyFile] using parsed_fy_py_file__and__folder_to_generate:
    property parsed_fy_py_files
    property folder_to_generate
fy"""

import abc
from functools import cached_property

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.fy_file.folder_to_generate.abc_fy import (
    FolderToGenerate_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.files_to_generate.abc_fy import (
    FilesToGenerate_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class FilesToGenerate_UsingParsedFyPyFile_And_FolderToGenerate_PropertyMixin(
    # Property Mixins
    FilesToGenerate_PropertyMixin_ABC,
    FolderToGenerate_PropertyMixin_ABC,
    ParsedFyPyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _files_to_generate(self) -> list[ParsedFyPyFile]:
        # fy:end <<<===
        return [
            parsed_file
            for parsed_file in self._parsed_fy_py_files
            if parsed_file.file_path.parent.is_relative_to(self._folder_to_generate)
            and parsed_file.file_type
            in {
                ParsedFyPyFileKind.FLOW,
                ParsedFyPyFileKind.METHOD,
                ParsedFyPyFileKind.PROPERTY,
            }
        ]
