import abc

from pathlib import Path


class With_FypyFileToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fypy_file_to_parse(self) -> Path:
        raise NotImplementedError()
