# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property mixin_imports_code: str using filtered_mixin_imports:
    property filtered_mixin_imports
"""

from functools import cached_property
from mixins.property.filtered_mixin_imports.abc_fy import (
    FilteredMixinImports_PropertyMixin_ABC,
)
import abc


# fy:start ===>>>
class MixinImportsCode_UsingFilteredMixinImports_PropertyMixin(
    # Property_mixins
    FilteredMixinImports_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_imports_code(self) -> str:
        # fy:end <<<===
        return "\n".join(
            sorted(self._filtered_mixin_imports)
            + ([""] if self._filtered_mixin_imports else [])
        )
