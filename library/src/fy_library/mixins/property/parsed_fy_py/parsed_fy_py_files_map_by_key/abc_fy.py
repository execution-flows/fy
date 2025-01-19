# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


property parsed_fy_py_files_map_by_key: dict[tuple[ParsedFyPyFileKind, str], ParsedFyPyFile]
fy"""

import abc

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


# fy:start ===>>>
class ParsedFyPyFilesMapByKey_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_py_files_map_by_key(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
