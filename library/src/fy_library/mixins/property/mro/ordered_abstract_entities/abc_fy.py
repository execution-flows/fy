# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


property abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int]
fy"""

import abc

from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


# fy:start ===>>>
class AbstractEntitiesOrderingIndex_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_entities_ordering_index(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], int]:
        raise NotImplementedError()
        # fy:end <<<===
