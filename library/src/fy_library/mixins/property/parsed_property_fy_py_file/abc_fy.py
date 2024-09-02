# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile


property parsed_property_fy_py_file: ParsedPropertyFyPyFile
"""

from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile
import abc


# fy:start ===>>>
class ParsedPropertyFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
