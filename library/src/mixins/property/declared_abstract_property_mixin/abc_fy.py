"""fy
from domain.fy_py_template_models import AbstractPropertyModel


property declared_abstract_property_mixin: AbstractPropertyModel
"""

from domain.fy_py_template_models import AbstractPropertyModel
import abc


# fy:start <<<===
class With_DeclaredAbstractPropertyMixin_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _declared_abstract_property_mixin(self) -> AbstractPropertyModel:
        raise NotImplementedError()
        # fy:end <<<===
