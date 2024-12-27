# fy:start ===>>>
from typing import List
from fy_library.domain.mixin_models import AbstractMethodModel


class AbstractMethodMixins_UsingSetter_PropertyMixin:
    @property
    def _abstract_method_mixins(self) -> List[AbstractMethodModel]:
        return self.__abstract_method_mixins

    @_abstract_method_mixins.setter
    def _abstract_method_mixins(
        self, abstract_method_mixins: List[AbstractMethodModel]
    ) -> None:
        self.__abstract_method_mixins = abstract_method_mixins


# fy:end <<<===
