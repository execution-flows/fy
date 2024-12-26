# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method method_required_2 -> str
"""

import abc


# fy:start ===>>>
class MethodRequired2_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _method_required_2(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
