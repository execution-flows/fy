# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters


property optional_flow_template_model_with_property_setters: FlowTemplateModelWithPropertySetters | None
"""

from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters
import abc


# fy:start ===>>>
class OptionalFlowTemplateModelWithPropertySetters_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _optional_flow_template_model_with_property_setters(
        self,
    ) -> FlowTemplateModelWithPropertySetters | None:
        raise NotImplementedError()
        # fy:end <<<===
