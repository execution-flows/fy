# fy:start ===>>>
from fy_library.mixins.property.imports_and_user_imports.import_flow_base.abc_fy import (
    ImportFlowBase_PropertyMixin_ABC,
)
from typing import List


class ImportFlowBase_UsingSetter_PropertyMixin(
    ImportFlowBase_PropertyMixin_ABC,
):
    @property
    def _import_flow_base(self) -> List[str]:
        return self.__import_flow_base

    @_import_flow_base.setter
    def _import_flow_base(self, import_flow_base: List[str]) -> None:
        self.__import_flow_base = import_flow_base


# fy:end <<<===
