# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property method_mixins_import: List[str] using method_mixins_and_mixin_import_map:
    property method_mixins
    property mixin_import_map
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.entity_key import entity_key
from fy_library.mixins.property.method_mixins.abc_fy import (
    MethodMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin(
    # Property_mixins
    MethodMixins_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _method_mixins_import(self) -> List[str]:
        # fy:end <<<===
        return [
            # method mixins
            self._mixin_import_map[
                entity_key(
                    mixin_name__snake_case=method_mixin.method_name.snake_case,
                    mixin_implementation_name__snake_case=method_mixin.implementation_name.snake_case,
                )
            ]
            for method_mixin in self._method_mixins
        ]
