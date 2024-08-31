# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from domain.fy_py_template_models import BaseTemplateModel


method generate_fy_py_code(jinja2_template: str, template_model: BaseTemplateModel) -> str using jinja2_templates:
"""
import pathlib

from jinja2 import Environment, FileSystemLoader

from domain.fy_py_template_models import BaseTemplateModel

_TEMPLATES_PATH = pathlib.Path(__file__).parent / "jinja2_templates"
_JINJA2_TEMPLATE_ENVIRONMENT = Environment(loader=FileSystemLoader(_TEMPLATES_PATH))


# fy:start ===>>>
class GenerateFyPyCode_UsingJinja2Templates_MethodMixin:
    def _generate_fy_py_code(
        self, jinja2_template: str, template_model: BaseTemplateModel
    ) -> str:
        # fy:end <<<===
        template = _JINJA2_TEMPLATE_ENVIRONMENT.get_template(jinja2_template)
        content = template.render(template_model.model_dump())
        return content
