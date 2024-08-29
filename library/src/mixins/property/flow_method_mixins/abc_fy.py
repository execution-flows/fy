"""fy
from domain.fy_py_template_models import MethodMixinModel
from typing import List


property flow_method_mixins: List[MethodMixinModel]
"""

from domain.fy_py_template_models import MethodMixinModel
from typing import List
import abc


# fy:start ===>>>
class With_FlowMethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _flow_method_mixins(self) -> List[MethodMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
