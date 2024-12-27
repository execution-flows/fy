# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_abstract_property_mixins: List[str] using abstract_property_mixin_and_mixin_import_map:
    property mixin_import_map
    property abstract_property_mixins
"""

from functools import cached_property
from typing import List

from fy_library.mixins.property.abstract_property_mixins.abc_fy import (
    AbstractPropertyMixins_PropertyMixin_ABC,
)
import abc


from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin(
    # Property_mixins
    AbstractPropertyMixins_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_abstract_property_mixins(self) -> List[str]:
        # fy:end <<<===
        return [
            # property mixins
            self._mixin_import_map[abstract_property_mixin.property_name.snake_case]
            for abstract_property_mixin in self._abstract_property_mixins
        ]
