# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property generate_fy_py_code: str
"""

import abc


# fy:start ===>>>
class GenerateFyPyCode_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _generate_fy_py_code(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
