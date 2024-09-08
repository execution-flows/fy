# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters


property optional_flow_template_model_with_property_setters: FlowTemplateModelWithPropertySetters | None using parsed_fy_py_file_and_property_setters_template_models:
    property parsed_fy_py_file
    property template_models
"""

from functools import cached_property
from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from fy_library.mixins.property.template_models.abc_fy import (
    TemplateModels_PropertyMixin_ABC,
)
import abc


# fy:start ===>>>
class OptionalFlowTemplateModelWithPropertySetters_UsingParsedFyPyFileAndPropertySettersTemplateModels_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    TemplateModels_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _optional_flow_template_model_with_property_setters(
        self,
    ) -> FlowTemplateModelWithPropertySetters | None:
        # fy:end <<<===
        if self._parsed_fy_py_file.file_type != ParsedFyPyFileKind.FLOW:
            return None

        return FlowTemplateModelWithPropertySetters.model_validate(
            {
                **self._parsed_fy_py_file.template_model.model_dump(),
                "property_setters": self._template_models,
            }
        )
