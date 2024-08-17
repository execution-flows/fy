from pathlib import Path

import abc


class With_FolderToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _folder_to_parse(self) -> Path:
        raise NotImplementedError()
