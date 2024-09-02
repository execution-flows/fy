# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from pathlib import Path
from typing import List


property fy_py_files_to_parse: List[Path]
"""

from pathlib import Path
from typing import List
import abc


# fy:start ===>>>
class FyPyFilesToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_files_to_parse(self) -> List[Path]:
        raise NotImplementedError()
        # fy:end <<<===
