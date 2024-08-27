"""fy
from domain.fy_py_template_models import AbstractPropertyModel
from typing import List


property declared_abstract_property_mixins: List[AbstractPropertyModel]
"""

from typing import List

from domain.fy_py_template_models import AbstractPropertyModel
import abc


# fy:start <<<===
class With_DeclaredAbstractPropertyMixin_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _declared_abstract_property_mixin(self) -> List[AbstractPropertyModel]:
        raise NotImplementedError()
        # fy:end <<<===
