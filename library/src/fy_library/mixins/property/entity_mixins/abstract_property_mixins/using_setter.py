# fy:start ===>>>
from typing import List
from fy_library.domain.mixin_models import AbstractPropertyModel


class AbstractPropertyMixins_UsingSetter_PropertyMixin:
    @property
    def _abstract_property_mixins(self) -> List[AbstractPropertyModel]:
        return self.__abstract_property_mixins

    @_abstract_property_mixins.setter
    def _abstract_property_mixins(
        self, abstract_property_mixins: List[AbstractPropertyModel]
    ) -> None:
        self.__abstract_property_mixins = abstract_property_mixins


# fy:end <<<===
