import abc

from pathlib import Path


class With_FyPyFileToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_file_to_parse(self) -> Path:
        raise NotImplementedError()
