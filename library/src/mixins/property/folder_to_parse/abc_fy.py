# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from pathlib import Path


property folder_to_parse: Path
"""

from pathlib import Path
import abc


# fy:start ===>>>
class FolderToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _folder_to_parse(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
