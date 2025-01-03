# fy:start ===>>>
class BaseFlowImport_UsingSetter_PropertyMixin:
    @property
    def _base_flow_import(self) -> str:
        return self.__base_flow_import

    @_base_flow_import.setter
    def _base_flow_import(self, base_flow_import: str) -> None:
        self.__base_flow_import = base_flow_import
        # fy:end <<<===
