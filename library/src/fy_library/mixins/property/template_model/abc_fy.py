# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel


property template_model: BaseTemplateModel
"""

import abc

from fy_library.domain.fy_py_template_models import BaseTemplateModel


# fy:start ===>>>
class TemplateModel_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _template_model(self) -> BaseTemplateModel:
        raise NotImplementedError()
        # fy:end <<<===
