# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow AbstractPropertyImportsFlow -> List[str]:
    property import_abc using constant
"""

from typing import List

from fy_core.base.flow_base import FlowBase


from fy_library.mixins.property.imports.import_abc__using_constant_fy import (
    ImportAbc_UsingConstant_PropertyMixin,
)


# fy:start ===>>>
class AbstractPropertyImportsFlow_Flow(
    # Property Mixins
    ImportAbc_UsingConstant_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __call__(self) -> List[str]:
        # fy:end <<<===
        return self._import_abc
