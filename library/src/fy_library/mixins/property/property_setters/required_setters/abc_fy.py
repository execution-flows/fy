# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


property required_setters: dict[str, PropertySetterFyPyFile]
fy"""

import abc

from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


# fy:start ===>>>
class RequiredSetters_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_setters(self) -> dict[str, PropertySetterFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
