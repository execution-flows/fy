# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property pre_fy_code: str
"""

import abc


# fy:start ===>>>
class PreFyCode_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _pre_fy_code(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
