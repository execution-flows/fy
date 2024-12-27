# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_abstract_method_mixins: List[str] using abstract_method_mixin_and_mixin_import_map:
    property mixin_import_map
    property abstract_method_mixins
"""

from functools import cached_property
from fy_library.mixins.property.abstract_method_mixins.abc_fy import (
    AbstractMethodMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start ===>>>
class ImportAbstractMethodMixins_UsingAbstractMethodMixinAndMixinImportMap_PropertyMixin(
    # Property_mixins
    AbstractMethodMixins_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_abstract_method_mixins(self) -> List[str]:
        # fy:end <<<===
        return [
            # method mixins
            self._mixin_import_map[abstract_method_mixin.method_name.snake_case]
            for abstract_method_mixin in self._abstract_method_mixins
        ]
