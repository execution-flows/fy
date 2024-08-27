# fy:start <<<===
from typing import List


class AbstractMethodFileSplit_UsingSetter_PropertyMixin:
    @property
    def _abstract_method_file_split(self) -> List[str]:
        return self.__abstract_method_file_split

    @_abstract_method_file_split.setter
    def _abstract_method_file_split(
        self, abstract_method_file_split: List[str]
    ) -> None:
        self.__abstract_method_file_split = abstract_method_file_split
        # fy:end <<<===
