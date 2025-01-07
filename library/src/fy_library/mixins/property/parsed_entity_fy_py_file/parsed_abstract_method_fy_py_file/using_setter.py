# fy:start ===>>>
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_abstract_method_fy_py_file.abc_fy import (
    ParsedAbstractMethodFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile


class ParsedAbstractMethodFyPyFile_UsingSetter_PropertyMixin(
    ParsedAbstractMethodFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_abstract_method_fy_py_file(self) -> ParsedAbstractMethodFyPyFile:
        return self.__parsed_abstract_method_fy_py_file

    @_parsed_abstract_method_fy_py_file.setter
    def _parsed_abstract_method_fy_py_file(
        self, parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile
    ) -> None:
        self.__parsed_abstract_method_fy_py_file = parsed_abstract_method_fy_py_file


# fy:end <<<===
