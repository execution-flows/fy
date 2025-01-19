# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property jinja2_template_file_name: str using property_setter_constant:
fy"""

import abc
from functools import cached_property

from fy_library.mixins.property.templates.jinja2_template_file_name.abc_fy import (
    Jinja2TemplateFileName_PropertyMixin_ABC,
)


# fy:start ===>>>
class Jinja2TemplateFileName_UsingPropertySetterConstant_PropertyMixin(
    # Property Mixins
    Jinja2TemplateFileName_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _jinja2_template_file_name(self) -> str:
        # fy:end <<<===
        return "property_setter.jinja2"
