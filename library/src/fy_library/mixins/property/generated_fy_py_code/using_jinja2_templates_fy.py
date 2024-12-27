# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property generated_fy_py_code: str using jinja2_templates:
    property template_model
    property jinja2_template_file_name
"""

import abc
import pathlib
from functools import cached_property
from typing import Final

import jinja2
from jinja2 import Environment, FileSystemLoader

from fy_library.mixins.property.generated_fy_py_code.abc_fy import (
    GeneratedFyPyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.jinja2_template_file_name.abc_fy import (
    Jinja2TemplateFileName_PropertyMixin_ABC,
)
from fy_library.mixins.property.template_model.abc_fy import (
    TemplateModel_PropertyMixin_ABC,
)

_TEMPLATES_PATH: Final = pathlib.Path(__file__).parent / "jinja2_templates"
_JINJA2_TEMPLATE_ENVIRONMENT: Final = Environment(
    loader=FileSystemLoader(_TEMPLATES_PATH),
    undefined=jinja2.StrictUndefined,
)


# fy:start ===>>>
class GeneratedFyPyCode_UsingJinja2Templates_PropertyMixin(
    # Property_mixins
    GeneratedFyPyCode_PropertyMixin_ABC,
    Jinja2TemplateFileName_PropertyMixin_ABC,
    TemplateModel_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _generated_fy_py_code(self) -> str:
        # fy:end <<<===
        template = _JINJA2_TEMPLATE_ENVIRONMENT.get_template(
            self._jinja2_template_file_name
        )
        content = template.render(self._template_model.model_dump())
        return content
