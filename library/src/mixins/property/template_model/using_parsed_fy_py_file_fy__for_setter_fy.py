# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from domain.fy_py_template_models import BaseTemplateModel


property template_model: BaseTemplateModel using parsed_fy_py_file__for_setter:
    property parsed_fy_py_file
"""

import abc
from functools import cached_property

from domain.fy_py_template_models import BaseTemplateModel
from mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class TemplateModel_UsingParsedFyPyFile_ForSetter_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _template_model(self) -> BaseTemplateModel:
        # fy:end <<<===
        return self._parsed_fy_py_file.template_model
