# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingParsedFyPyFile -> None:
    property parsed_fy_py_file using setter
    property mixin_import_map using setter
    property mixin_imports using parsed_fy_py_file
    property jinja2_template_file_name using parsed_fy_py_file
    property generate_fy_py_code using jinja2_templates
    property filtered_mixin_imports using remove_existing_imports
    property mixin_imports_code using filtered_mixin_imports
    property fy_py_file_content using parsed_fy_py_file
    method generate_and_save_fy_py_code using parsed_fy_py_file__and__fy_py_file_content
"""
from typing import Any, Dict

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from mixins.property.filtered_mixin_imports.remove_existing_imports_fy import (
    FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin,
)
from mixins.property.fy_py_file_content.using_parsed_fy_py_file_fy import (
    FyPyFileContent_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.generated_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
)
from mixins.property.jinja2_template_file_name.using_parsed_fy_py_file_fy import (
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from mixins.property.mixin_imports.using_parsed_fy_py_file_fy import (
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.mixin_imports_code.using_filtered_mixin_imports_fy import (
    MixinImportsCode_UsingFilteredMixinImports_PropertyMixin,
)
from mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


from mixins.method.generate_and_save_fy_py_code.using_parsed_fy_py_file__and__fy_py_file_content_fy import (
    GenerateAndSaveFyPyCode_UsingParsedFyPyFile_And_FyPyFileContent_MethodMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
    FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin,
    MixinImportsCode_UsingFilteredMixinImports_PropertyMixin,
    FyPyFileContent_UsingParsedFyPyFile_PropertyMixin,
    # Method Mixins
    GenerateAndSaveFyPyCode_UsingParsedFyPyFile_And_FyPyFileContent_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        self._generate_and_save_fy_py_code()

    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        mixin_import_map: Dict[str, str],
        **kwargs: Any,
    ):
        self._mixin_import_map = mixin_import_map
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)
