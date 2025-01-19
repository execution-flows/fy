# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


property parsed_fy_py_files_map_by_key: dict[tuple[ParsedFyPyFileKind, str], ParsedFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
fy"""

import abc
from functools import cached_property

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin(
    # Property Mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files_map_by_key(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], ParsedFyPyFile]:
        # fy:end <<<===
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ] = {}
        for parsed_fy_py_file in self._parsed_fy_py_files:
            if parsed_fy_py_file.entity_key in parsed_fy_py_files_map_by_key:
                raise AssertionError(
                    f"Duplicate key {parsed_fy_py_file.entity_key} found."
                )
            parsed_fy_py_files_map_by_key[parsed_fy_py_file.entity_key] = (
                parsed_fy_py_file
            )

        return parsed_fy_py_files_map_by_key
