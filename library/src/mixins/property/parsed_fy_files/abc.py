import abc
from typing import List

from domain.parsed_fy_file import ParsedFyFile


class With_ParsedFyFiles_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_files(self) -> List[ParsedFyFile]:
        raise NotImplementedError()
