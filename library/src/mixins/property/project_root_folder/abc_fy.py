# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from pathlib import Path


property project_root_folder: Path
"""

import abc
from pathlib import Path


# fy:start ===>>>
class ProjectRootFolder_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _project_root_folder(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
