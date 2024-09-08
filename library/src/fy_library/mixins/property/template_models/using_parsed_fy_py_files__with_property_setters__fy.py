# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel
from typing import List


property template_models: List[BaseTemplateModel] using parsed_fy_py_files__with_property_setters:
    property parsed_fy_py_files
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.fy_py_template_models import (
    BaseTemplateModel,
)
from fy_library.mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class TemplateModels_UsingParsedFyPyFiles_WithPropertySetters_PropertyMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _template_models(self) -> List[BaseTemplateModel]:
        # fy:end <<<===
        return [
            abstract_property_setter.template_model
            for abstract_property_setter in self._parsed_fy_py_files
        ]
