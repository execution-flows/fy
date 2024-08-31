# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


method remove_existing_imports(mixin_imports: List[str], pre_marker_file_content: str, user_imports: str) -> List[str]
"""

from typing import List
import abc


# fy:start ===>>>
class RemoveExistingImports_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _remove_existing_imports(
        self, mixin_imports: List[str], pre_marker_file_content: str, user_imports: str
    ) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
