import abc

from domain.parsed_fy_py_file import ParsedFyPyFileKind


class With_FyFileKind_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        raise NotImplementedError()