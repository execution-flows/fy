# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property property_mixins_import: List[str] using property_mixins_and_mixin_import_map:
    property property_mixins
    property mixin_import_map
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.entity_key import entity_key
from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_mixins.abc_fy import (
    PropertyMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin(
    # Property_mixins
    MixinImportMap_PropertyMixin_ABC,
    PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_mixins_import(self) -> List[str]:
        # fy:end <<<===
        return [
            # property mixins
            self._mixin_import_map[
                entity_key(
                    mixin_name__snake_case=property_mixin.property_name.snake_case,
                    mixin_implementation_name__snake_case=property_mixin.implementation_name.snake_case,
                )
            ]
            for property_mixin in self._property_mixins
        ]
