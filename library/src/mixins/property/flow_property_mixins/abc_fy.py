"""fy
from domain.fy_py_template_models import PropertyMixinModel
from typing import List


property flow_property_mixins: List[PropertyMixinModel]
"""

from domain.fy_py_template_models import PropertyMixinModel
from typing import List
import abc


# fy:start ===>>>
class With_FlowPropertyMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _flow_property_mixins(self) -> List[PropertyMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
