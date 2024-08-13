# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
from typing import Dict


class With_MixinImportMap_PropertyMixin_ABC(abc.ABC):

    @property
    @abc.abstractmethod
    def _mixin_import_map(self) -> Dict[str, str]:
        raise NotImplementedError()
