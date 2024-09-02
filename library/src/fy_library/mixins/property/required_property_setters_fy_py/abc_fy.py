# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property required_property_setters_fy_py: List[ParsedFyPyFile]
"""

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from typing import List
import abc


# fy:start ===>>>
class RequiredPropertySettersFyPy_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
