# fy:start ===>>>
from typing import List


class ImportFlowBase_UsingSetter_PropertyMixin:
    @property
    def _import_flow_base(self) -> List[str]:
        return self.__import_flow_base

    @_import_flow_base.setter
    def _import_flow_base(self, import_flow_base: List[str]) -> None:
        self.__import_flow_base = import_flow_base


# fy:end <<<===
