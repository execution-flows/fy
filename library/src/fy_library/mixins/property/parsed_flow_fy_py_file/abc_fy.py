# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile


property parsed_flow_fy_py_file: ParsedFlowFyPyFile
"""

from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile
import abc


# fy:start ===>>>
class ParsedFlowFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_flow_fy_py_file(self) -> ParsedFlowFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
