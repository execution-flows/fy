# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List



property import_base_flow: List[str] using declared_base_flow_name:
    property declared_base_flow_name
    property mixin_import_map
"""

from functools import cached_property

import abc
from typing import List

from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)

from fy_library.mixins.property.declared_base_flow_name.abc_fy import (
    DeclaredBaseFlowName_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportBaseFlow_UsingDeclaredBaseFlowName_PropertyMixin(
    # Property_mixins
    DeclaredBaseFlowName_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_base_flow(self) -> List[str]:
        # fy:end <<<===
        if self._declared_base_flow_name == "":
            return []
        return [self._mixin_import_map[self._declared_base_flow_name.lower()]]
