import abc

from typing import Dict


class With_MixinImportMap_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_import_map(self) -> Dict[str, str]:
        raise NotImplementedError()
