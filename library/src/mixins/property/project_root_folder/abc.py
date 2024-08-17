import abc

from pathlib import Path


class With_ProjectRootFolder_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _project_root_folder(self) -> Path:
        raise NotImplementedError()
