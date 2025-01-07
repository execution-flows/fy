# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


property required_property_setters_fy_py_with_own_abstract_mixin: list[PropertySetterFyPyFile]
fy"""

import abc

from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


# fy:start ===>>>
class RequiredPropertySettersFyPyWithOwnAbstractMixin_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_property_setters_fy_py_with_own_abstract_mixin(
        self,
    ) -> list[PropertySetterFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
