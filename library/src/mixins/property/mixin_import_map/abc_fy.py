"""fy
from typing import Dict


property mixin_import_map: Dict[str, str]

"""

from typing import Dict
import abc


# fy:start <<<===
class With_MixinImportMap_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_import_map(self) -> Dict[str, str]:
        raise NotImplementedError()
        # fy:end <<<===
