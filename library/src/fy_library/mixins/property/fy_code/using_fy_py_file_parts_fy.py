# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property fy_code: str using fy_py_file_parts:
    property fy_py_file_parts
"""

import abc
from functools import cached_property

from fy_library.mixins.property.fy_py_file_parts.abc_fy import (
    FyPyFileParts_PropertyMixin_ABC,
)

from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyCode_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_code(self) -> str:
        # fy:end <<<===
        fy_code = self._fy_py_file_parts.fy_code
        return fy_code
