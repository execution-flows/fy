"""fy
from domain.fy_py_template_models import AbstractMethodModel, MethodMixinModel
from typing import List


property method_mixins: List[AbstractMethodModel]
"""

import abc
from typing import List

from domain.fy_py_template_models import AbstractMethodModel


# fy:start ===>>>
class With_MethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_mixins(self) -> List[AbstractMethodModel]:
        raise NotImplementedError()
        # fy:end <<<===
