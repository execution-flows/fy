# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files_with_own_abstract_mixin: List[ParsedFyPyFile]
"""

import abc
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


# fy:start ===>>>
class ParsedFyPyFilesWithOwnAbstractMixin_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_py_files_with_own_abstract_mixin(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
