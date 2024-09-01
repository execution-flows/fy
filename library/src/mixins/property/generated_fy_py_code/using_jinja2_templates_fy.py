# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property generate_fy_py_code: str using jinja2_templates:
    property parsed_fy_py_file
    property jinja2_template_file_name
"""
import pathlib
from typing import Final

from jinja2 import Environment, FileSystemLoader
from functools import cached_property
from mixins.property.jinja2_template_file_name.abc_fy import (
    Jinja2TemplateFileName_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
import abc

_TEMPLATES_PATH: Final = pathlib.Path(__file__).parent / "jinja2_templates"
_JINJA2_TEMPLATE_ENVIRONMENT: Final = Environment(
    loader=FileSystemLoader(_TEMPLATES_PATH)
)


# fy:start ===>>>
class GenerateFyPyCode_UsingJinja2Templates_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    Jinja2TemplateFileName_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _generate_fy_py_code(self) -> str:
        # fy:end <<<===
        template = _JINJA2_TEMPLATE_ENVIRONMENT.get_template(
            self._jinja2_template_file_name
        )
        content = template.render(self._parsed_fy_py_file.template_model.model_dump())
        return content
