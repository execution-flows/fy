"""fy
property included_mixins: IncludedMixinsModel
"""

import abc
from typing import List

from pydantic import BaseModel

from domain.fy_py_template_models import (
    AbstractMethodModel,
    AbstractPropertyModel,
    MethodMixinModel,
    PropertyMixinModel,
)


class IncludedMixinsModel(BaseModel):
    abstract_method_mixins: List[AbstractMethodModel]
    abstract_property_mixins: List[AbstractPropertyModel]
    method_mixins: List[MethodMixinModel]
    property_mixins: List[PropertyMixinModel]


# fy:start ===>>>
class With_IncludedMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _included_mixins(self) -> IncludedMixinsModel:
        raise NotImplementedError()
        # fy:end <<<===
