import abc

from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile


class With_ParsedFyPyFiles_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
