# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property fy_py_file_content: str using parsed_fy_py_file:
    property parsed_fy_py_file
    property mixin_imports_code
    property generate_fy_py_code
"""

import abc
from functools import cached_property

from constants import (
    FY_CODE_FILE_END_SIGNATURE,
    FY_PY_FILE_SIGNATURE,
    NEW_LINE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from mixins.property.generated_fy_py_code.abc_fy import (
    GenerateFyPyCode_PropertyMixin_ABC,
)
from mixins.property.mixin_imports_code.abc_fy import (
    MixinImportsCode_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyPyFileContent_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    MixinImportsCode_PropertyMixin_ABC,
    GenerateFyPyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_content(self) -> str:
        # fy:end <<<===
        fy_py_file_content = (
            f"{self._parsed_fy_py_file.pre_fy_code}"
            f"{FY_PY_FILE_SIGNATURE}"
            f"{self._parsed_fy_py_file.fy_code}"
            f"{FY_CODE_FILE_END_SIGNATURE}\n"
            f"{self._parsed_fy_py_file.pre_marker_file_content}"
            f"{NEW_LINE if not self._parsed_fy_py_file.pre_marker_file_content or self._mixin_imports_code else ''}"
            f"{self._mixin_imports_code}"
            f"{NEW_LINE * 2 if not self._parsed_fy_py_file.pre_marker_file_content or self._mixin_imports_code else ''}"
            f"{FY_START_MARKER}\n"
            f"{self._generate_fy_py_code}"
            f"{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )

        return fy_py_file_content
