# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow generate_and_save_fy_py_file__using_required_property_setters -> None:
    property parsed_fy_py_file using setter
    property import_generic using constant(["from typing import Generic"])
    property jinja2_template_file_name using property_setter_constant
    property template_model using parsed_fy_py_file__for_setter
    property generated_fy_py_code using jinja2_templates
    property fy_py_file_content using required_property_setter
    method generate_and_save_fy_py_code using parsed_fy_py_file__and__fy_py_file_content
fy"""

from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.method.generate_and_save_fy_py_code.using_parsed_fy_py_file__and__fy_py_file_content_fy import (
    GenerateAndSaveFyPyCode_UsingParsedFyPyFile_And_FyPyFileContent_MethodMixin,
)
from fy_library.mixins.property.fy_py_file.fy_py_file_content.using_required_property_setter_fy import (
    FyPyFileContent_UsingRequiredPropertySetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.import_generic.using_setter import (
    ImportGeneric_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.templates.generated_fy_py_code.using_jinja2_templates_fy import (
    GeneratedFyPyCode_UsingJinja2Templates_PropertyMixin,
)
from fy_library.mixins.property.templates.jinja2_template_file_name.using_property_setter_constant_fy import (
    Jinja2TemplateFileName_UsingPropertySetterConstant_PropertyMixin,
)
from fy_library.mixins.property.templates.template_model.using_parsed_fy_py_file_fy__for_setter_fy import (
    TemplateModel_UsingParsedFyPyFile_ForSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingRequiredPropertySetters_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ImportGeneric_UsingSetter_PropertyMixin,
    Jinja2TemplateFileName_UsingPropertySetterConstant_PropertyMixin,
    TemplateModel_UsingParsedFyPyFile_ForSetter_PropertyMixin,
    GeneratedFyPyCode_UsingJinja2Templates_PropertyMixin,
    FyPyFileContent_UsingRequiredPropertySetter_PropertyMixin,
    # Method Mixins
    GenerateAndSaveFyPyCode_UsingParsedFyPyFile_And_FyPyFileContent_MethodMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._import_generic = ["from typing import Generic"]
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        self._generate_and_save_fy_py_code()
