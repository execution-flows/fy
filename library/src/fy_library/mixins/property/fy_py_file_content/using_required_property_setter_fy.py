# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property fy_py_file_content: str using required_property_setter:
    property parsed_fy_py_file
    property generated_fy_py_code
    property import_generic
"""

import abc
from functools import cached_property
from typing import Final

from fy_library.constants import FY_START_MARKER, FY_END_MARKER
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile
from fy_library.mixins.property.fy_py_file_content.abc_fy import (
    FyPyFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.generated_fy_py_code.abc_fy import (
    GeneratedFyPyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports.import_generic__abc_fy import (
    ImportGeneric_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

_NEW_LINE: Final = "\n"


# fy:start ===>>>
class FyPyFileContent_UsingRequiredPropertySetter_PropertyMixin(
    # Property_mixins
    FyPyFileContent_PropertyMixin_ABC,
    GeneratedFyPyCode_PropertyMixin_ABC,
    ImportGeneric_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_content(self) -> str:
        # fy:end <<<===
        assert isinstance(self._parsed_fy_py_file, PropertySetterFyPyFile)

        fy_py_file_content = (
            f"{FY_START_MARKER}\n"
            f"{self._import_generic[0] + _NEW_LINE if self._parsed_fy_py_file.generics_def != '' else ''}"
            f"{self._parsed_fy_py_file.user_imports}"
            f"{self._generated_fy_py_code}"
            f"{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )
        return fy_py_file_content
