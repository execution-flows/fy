"""fy
from domain.fy_py_template_models import AbstractMethodModel
from typing import List


property declared_abstract_method_mixin: List[AbstractMethodModel]
"""

from domain.fy_py_template_models import AbstractMethodModel
from typing import List
import abc


# fy:start <<<===
class With_DeclaredAbstractMethodMixin_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _declared_abstract_method_mixin(self) -> List[AbstractMethodModel]:
        raise NotImplementedError()
        # fy:end <<<===
