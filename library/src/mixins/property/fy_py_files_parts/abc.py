import abc
from domain.parsed_fy_py_file import FyPyFileParts


class With_FyPyFilesParts_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_files_parts(self) -> FyPyFileParts:
        raise NotImplementedError()
