import abc

from domain.parsed_fy_py_file import FyPyFileParts


class With_FyPyFileParts_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_file_parts(self) -> FyPyFileParts:
        raise NotImplementedError()
