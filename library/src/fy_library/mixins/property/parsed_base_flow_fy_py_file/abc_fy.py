# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedBaseFlowFyPyFile


property parsed_base_flow_fy_py_file: ParsedBaseFlowFyPyFile
"""

from fy_library.domain.parsed_fy_py_file import ParsedBaseFlowFyPyFile
import abc


# fy:start ===>>>
class ParsedBaseFlowFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_base_flow_fy_py_file(self) -> ParsedBaseFlowFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
