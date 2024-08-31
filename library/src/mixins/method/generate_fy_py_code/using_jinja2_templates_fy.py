# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


method generate_fy_py_code(jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile) -> str using jinja2_templates:
"""
import pathlib

from jinja2 import Environment, FileSystemLoader

from domain.parsed_fy_py_file import ParsedFyPyFile


# fy:start ===>>>
class GenerateFyPyCode_UsingJinja2Templates_MethodMixin:
    def _generate_fy_py_code(
        self, jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
    ) -> str:
        # fy:end <<<===
        templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
        env = Environment(loader=FileSystemLoader(templates_path))
        template = env.get_template(jinja2_template)
        template_model = parsed_fy_py_file.template_model.model_dump()
        content = template.render(template_model)
        return content
