import abc
from pathlib import Path
from typing import List


class With_FyFilesToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_files_to_parse(self) -> List[Path]:
        raise NotImplementedError()