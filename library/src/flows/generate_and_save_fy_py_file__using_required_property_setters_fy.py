# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingRequiredPropertySetters -> None:
    property parsed_fy_py_file using setter
    property jinja2_template_file_name using property_setter_constant
    property generate_fy_py_code using jinja2_templates
"""
from typing import Any

from base.flow_base import FlowBase
from constants import FY_START_MARKER, FY_END_MARKER
from domain.parsed_fy_py_file import ParsedFyPyFile
from mixins.property.generated_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
)
from mixins.property.jinja2_template_file_name.using_property_setter_constant_fy import (
    Jinja2TemplateFileName_UsingPropertySetterConstant_PropertyMixin,
)
from mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingRequiredPropertySetters_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    Jinja2TemplateFileName_UsingPropertySetterConstant_PropertyMixin,
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        fy_py_file_content = (
            f"{FY_START_MARKER}\n"
            f"{self._parsed_fy_py_file.user_imports}"
            f"{self._generate_fy_py_code}"
            f"{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )
        with open(
            file=self._parsed_fy_py_file.file_path, mode="w", encoding="UTF-8"
        ) as setter_file:
            setter_file.write(fy_py_file_content)

    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)
