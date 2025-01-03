# fy:start ===>>>
from typing import List
from fy_library.domain.mixin_models import MethodMixinModel


class MethodMixins_UsingSetter_PropertyMixin:
    @property
    def _method_mixins(self) -> List[MethodMixinModel]:
        return self.__method_mixins

    @_method_mixins.setter
    def _method_mixins(self, method_mixins: List[MethodMixinModel]) -> None:
        self.__method_mixins = method_mixins


# fy:end <<<===
