"""fy
from domain.fy_py_template_models import AbstractMethodModel
from typing import List


property declared_abstract_method_mixins: List[AbstractMethodModel]
"""

from domain.fy_py_template_models import AbstractMethodModel
from typing import List
import abc


# fy:start <<<===
class With_DeclaredAbstractMethodMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _declared_abstract_method_mixins(self) -> List[AbstractMethodModel]:
        raise NotImplementedError()
        # fy:end <<<===
