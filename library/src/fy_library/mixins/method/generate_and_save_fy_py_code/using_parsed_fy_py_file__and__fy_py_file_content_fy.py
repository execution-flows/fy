# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method generate_and_save_fy_py_code -> None using parsed_fy_py_file__and__fy_py_file_content:
    property parsed_fy_py_file
    property fy_py_file_content
"""

import abc

from fy_library.mixins.property.fy_py_file_content.abc_fy import (
    FyPyFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class GenerateAndSaveFyPyCode_UsingParsedFyPyFile_And_FyPyFileContent_MethodMixin(
    # Property_mixins
    FyPyFileContent_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_fy_py_code(self) -> None:
        # fy:end <<<===
        fy_py_file_content = self._fy_py_file_content
        with open(
            file=self._parsed_fy_py_file.file_path, mode="w", encoding="UTF-8"
        ) as setter_file:
            setter_file.write(fy_py_file_content)
