# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile


property parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile
"""

from fy_library.domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile
import abc


# fy:start ===>>>
class ParsedAbstractMethodFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_abstract_method_fy_py_file(self) -> ParsedAbstractMethodFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
