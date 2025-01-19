# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property method_mixins_import: list[str] using method_mixins_and_mixin_import_map:
    property method_mixins
    property mixin_import_map
fy"""

import abc
from functools import cached_property

from fy_library.mixins.property.entity_mixins.method_mixins.abc_fy import (
    MethodMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin(
    # Property Mixins
    MethodMixins_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_mixins_import(self) -> list[str]:
        # fy:end <<<===
        return [
            # method mixins
            self._mixin_import_map[method_mixin.entity_key]
            for method_mixin in self._method_mixins
        ]
