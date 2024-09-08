# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseFlowTemplateModelWithPropertySetters


property optional_base_flow_template_model_with_property_setters: BaseFlowTemplateModelWithPropertySetters | None
"""

import abc

from fy_library.domain.fy_py_template_models import (
    BaseFlowTemplateModelWithPropertySetters,
)


# fy:start ===>>>
class OptionalBaseFlowTemplateModelWithPropertySetters_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _optional_base_flow_template_model_with_property_setters(
        self,
    ) -> BaseFlowTemplateModelWithPropertySetters | None:
        raise NotImplementedError()
        # fy:end <<<===
