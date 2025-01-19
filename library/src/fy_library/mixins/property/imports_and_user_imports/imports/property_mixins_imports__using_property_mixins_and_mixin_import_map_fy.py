# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_mixins_import: list[str] using property_mixins_and_mixin_import_map:
    property property_mixins
    property mixin_import_map
fy"""

import abc
from functools import cached_property

from fy_library.mixins.property.entity_mixins.property_mixins.abc_fy import (
    PropertyMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin(
    # Property Mixins
    MixinImportMap_PropertyMixin_ABC,
    PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_mixins_import(self) -> list[str]:
        # fy:end <<<===
        return [
            # property mixins
            self._mixin_import_map[property_mixin.entity_key]
            for property_mixin in self._property_mixins
        ]
