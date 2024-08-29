"""fy
from domain.fy_py_template_models import AbstractPropertyModel, PropertyMixinModel
from typing import List


property property_mixins: List[AbstractPropertyModel]
"""

import abc
from typing import List

from domain.fy_py_template_models import AbstractPropertyModel


# fy:start ===>>>
class With_PropertyMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _property_mixins(self) -> List[AbstractPropertyModel]:
        raise NotImplementedError()
        # fy:end <<<===
