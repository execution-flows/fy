# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


property mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str]
fy"""

import abc

from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


# fy:start ===>>>
class MixinImportMap_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_import_map(self) -> dict[tuple[ParsedFyPyFileKind, str], str]:
        raise NotImplementedError()
        # fy:end <<<===
