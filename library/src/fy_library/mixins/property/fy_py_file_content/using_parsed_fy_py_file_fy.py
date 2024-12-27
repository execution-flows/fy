# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property fy_py_file_content: str using parsed_fy_py_file:
    property parsed_fy_py_file
    property mixin_imports_code
    property generated_fy_py_code
"""

import abc
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_CODE_FILE_END_SIGNATURE,
    FY_PY_FILE_SIGNATURE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.fy_py_file_content.abc_fy import (
    FyPyFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.generated_fy_py_code.abc_fy import (
    GeneratedFyPyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_imports_code.abc_fy import (
    MixinImportsCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

_NEW_LINE: Final = "\n"


# fy:start ===>>>
class FyPyFileContent_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    FyPyFileContent_PropertyMixin_ABC,
    GeneratedFyPyCode_PropertyMixin_ABC,
    MixinImportsCode_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_content(self) -> str:
        # fy:end <<<===
        stripped_pre_marker_file_content = (
            self._parsed_fy_py_file.pre_marker_file_content.strip()
        )
        end_marker_space = (
            " " * 4
            if self._parsed_fy_py_file.file_type == ParsedFyPyFileKind.BASE_FLOW
            else " " * 8
        )
        fy_py_file_content = (
            f"{self._parsed_fy_py_file.pre_fy_code}"
            f"{FY_PY_FILE_SIGNATURE}"
            f"{self._parsed_fy_py_file.fy_code}"
            f"{FY_CODE_FILE_END_SIGNATURE}\n"
            f"{_NEW_LINE if stripped_pre_marker_file_content else ''}"
            f"{stripped_pre_marker_file_content}"
            f"{_NEW_LINE if stripped_pre_marker_file_content else ''}"
            f"{_NEW_LINE if self._mixin_imports_code else ''}"
            f"{self._mixin_imports_code}"
            f"\n\n{FY_START_MARKER}\n"
            f"{self._generated_fy_py_code}"
            f"{end_marker_space}{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )

        return fy_py_file_content
