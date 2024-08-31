# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method generate_and_save_fy_py_files -> None using parsed_fy_py_files:
    property parsed_fy_py_files
    property mixin_import_map
    method generate_fy_py_code
"""
import abc

from mixins.method.generate_fy_py_code.abc_fy import (
    GenerateFyPyCode_MethodMixin_ABC,
)
from mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles_MethodMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    # Method_mixins
    GenerateFyPyCode_MethodMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_fy_py_files(self) -> None:
        # fy:end <<<===
        pass
