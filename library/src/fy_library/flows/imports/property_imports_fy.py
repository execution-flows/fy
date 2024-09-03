# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow PropertyImports -> List[str]:
    property cached_import using constant
"""

from typing import List

from fy_core.base.flow_base import FlowBase
from fy_library.mixins.property.imports.cached_import__using_constant_fy import (
    CachedImport_UsingConstant_PropertyMixin,
)


# fy:start ===>>>
class PropertyImports_Flow(
    # Property Mixins
    CachedImport_UsingConstant_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __call__(self) -> List[str]:
        # fy:end <<<===
        return self._cached_import
