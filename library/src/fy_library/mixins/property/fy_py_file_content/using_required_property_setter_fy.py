# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property fy_py_file_content: str using required_property_setter:
    property parsed_fy_py_file
    property generated_fy_py_code
"""

import abc
from functools import cached_property

from fy_library.constants import FY_START_MARKER, FY_END_MARKER
from fy_library.mixins.property.generated_fy_py_code.abc_fy import (
    GeneratedFyPyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyPyFileContent_UsingRequiredPropertySetter_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    GeneratedFyPyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_content(self) -> str:
        # fy:end <<<===
        fy_py_file_content = (
            f"{FY_START_MARKER}\n"
            f"{self._parsed_fy_py_file.user_imports}"
            f"{self._generated_fy_py_code}"
            f"{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )
        return fy_py_file_content
