# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingRequiredPropertySetters -> None:
    property parsed_fy_py_file using setter
    method generate_fy_py_code using jinja2_templates
"""
from typing import Any

from base.flow_base import FlowBase
from constants import FY_START_MARKER, FY_END_MARKER
from domain.parsed_fy_py_file import ParsedFyPyFile
from mixins.method.generate_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
)
from mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingRequiredPropertySetters_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    # Method Mixins
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        generated_python_code = self._generate_fy_py_code(
            jinja2_template="property_setter.jinja2",
            template_model=self._parsed_fy_py_file.template_model,
        )
        fy_py_file_content = (
            f"{FY_START_MARKER}\n"
            f"{self._parsed_fy_py_file.user_imports}"
            f"{generated_python_code}"
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
