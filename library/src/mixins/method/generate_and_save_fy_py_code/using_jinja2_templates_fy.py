# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method generate_and_save_fy_py_files -> None using jinja2_templates:
    property parsed_fy_py_files
    property required_property_setters_fy_py
    property mixin_import_map
    method generate_and_save_fy_py_files
"""

import abc

from flows.generate_and_save_fy_py_files__using_required_property_setters_fy import (
    GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow,
)
from mixins.method.generate_and_save_fy_py_files.abc_fy import (
    GenerateAndSaveFyPyFiles_MethodMixin_ABC,
)
from mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.required_property_setters_fy_py.abc_fy import (
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingJinja2Templates_MethodMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    # Method_mixins
    GenerateAndSaveFyPyFiles_MethodMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_fy_py_files(self) -> None:
        # fy:end <<<===
        self._generate_and_save_fy_py_files()
        GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow(
            required_property_setters_fy_py=self._required_property_setters_fy_py
        )()
