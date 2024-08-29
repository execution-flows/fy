"""fy
from domain.fy_py_template_models import AbstractMethodModel, MethodMixinModel
from typing import List


property method_mixins: List[AbstractMethodModel]
"""

from domain.fy_py_template_models import AbstractMethodModel, MethodMixinModel
from typing import List
import abc


# fy:start ===>>>
class With_MethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_mixins(self) -> List[AbstractMethodModel] | List[MethodMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
