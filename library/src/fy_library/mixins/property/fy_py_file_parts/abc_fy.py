# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import FyPyFileParts


property fy_py_file_parts: FyPyFileParts
"""

from fy_library.domain.parsed_fy_py_file import FyPyFileParts
import abc


# fy:start ===>>>
class FyPyFileParts_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_file_parts(self) -> FyPyFileParts:
        raise NotImplementedError()
        # fy:end <<<===
