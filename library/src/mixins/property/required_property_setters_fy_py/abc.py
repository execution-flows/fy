import abc

from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile


class With_RequiredPropertySettersFyPy_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
