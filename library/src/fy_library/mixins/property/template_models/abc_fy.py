# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel
from typing import List


property template_models: List[BaseTemplateModel]
"""

import abc
from typing import List

from fy_library.domain.fy_py_template_models import BaseTemplateModel


# fy:start ===>>>
class TemplateModels_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _template_models(self) -> List[BaseTemplateModel]:
        raise NotImplementedError()
        # fy:end <<<===
