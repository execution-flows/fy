# fy:start ===>>>
from typing import List
from fy_library.domain.mixin_models import PropertyMixinModel


class PropertyMixins_UsingSetter_PropertyMixin:
    @property
    def _property_mixins(self) -> List[PropertyMixinModel]:
        return self.__property_mixins

    @_property_mixins.setter
    def _property_mixins(self, property_mixins: List[PropertyMixinModel]) -> None:
        self.__property_mixins = property_mixins


# fy:end <<<===
