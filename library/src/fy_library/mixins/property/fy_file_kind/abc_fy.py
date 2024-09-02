# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind


property fy_file_kind: ParsedFyPyFileKind
"""

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
import abc


# fy:start ===>>>
class FyFileKind_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        raise NotImplementedError()
        # fy:end <<<===
