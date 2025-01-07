# fy:start ===>>>
from fy_library.mixins.property.entity_mixins.abstract_method_mixins.abc_fy import (
    AbstractMethodMixins_PropertyMixin_ABC,
)
from typing import List
from fy_library.domain.mixin_models import AbstractMethodModel


class AbstractMethodMixins_UsingSetter_PropertyMixin(
    AbstractMethodMixins_PropertyMixin_ABC,
):
    @property
    def _abstract_method_mixins(self) -> List[AbstractMethodModel]:
        return self.__abstract_method_mixins

    @_abstract_method_mixins.setter
    def _abstract_method_mixins(
        self, abstract_method_mixins: List[AbstractMethodModel]
    ) -> None:
        self.__abstract_method_mixins = abstract_method_mixins


# fy:end <<<===
