# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters -> None:
    property required_property_setters_fy_py using setter
"""
import pathlib
from typing import Any, List

from jinja2 import FileSystemLoader, Environment

from base.flow_base import FlowBase
from constants import FY_START_MARKER, FY_END_MARKER
from domain.parsed_fy_py_file import ParsedFyPyFile

from mixins.property.required_property_setters_fy_py.using_setter import (
    RequiredPropertySettersFyPy_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow(
    # Property Mixins
    RequiredPropertySettersFyPy_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        for parsed_fy_py_file in self._required_property_setters_fy_py:
            generated_python_code = generated_fy_py_code(
                jinja2_template="property_setter.jinja2",
                parsed_fy_py_file=parsed_fy_py_file,
            )
            fy_py_file_content = (
                f"{FY_START_MARKER}\n"
                f"{parsed_fy_py_file.user_imports}"
                f"{generated_python_code}"
                f"{FY_END_MARKER}\n"
                f"{parsed_fy_py_file.post_marker_file_content}"
            )
            with open(
                file=parsed_fy_py_file.file_path, mode="w", encoding="UTF-8"
            ) as setter_file:
                setter_file.write(fy_py_file_content)

    def __init__(
        self,
        *args: Any,
        required_property_setters_fy_py: List[ParsedFyPyFile],
        **kwargs: Any,
    ):
        self._required_property_setters_fy_py = required_property_setters_fy_py
        super().__init__(*args, **kwargs)


def generated_fy_py_code(
    jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
) -> str:
    templates_path = str(pathlib.Path(__file__).parent.parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template)
    template_model = parsed_fy_py_file.template_model.model_dump()
    content = template.render(template_model)
    return content
