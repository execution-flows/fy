# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile


class ParsedAbstractPropertyFyPyFile_UsingSetter_PropertyMixin:
    @property
    def _parsed_abstract_property_fy_py_file(self) -> ParsedAbstractPropertyFyPyFile:
        return self.__parsed_abstract_property_fy_py_file

    @_parsed_abstract_property_fy_py_file.setter
    def _parsed_abstract_property_fy_py_file(
        self, parsed_abstract_property_fy_py_file: ParsedAbstractPropertyFyPyFile
    ) -> None:
        self.__parsed_abstract_property_fy_py_file = parsed_abstract_property_fy_py_file


# fy:end <<<===
