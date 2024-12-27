# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property mixin_imports_code: str using filtered_mixin_imports:
    property filtered_mixin_imports
"""

import abc
from functools import cached_property

from fy_library.mixins.property.filtered_mixin_imports.abc_fy import (
    FilteredMixinImports_PropertyMixin_ABC,
)

from fy_library.mixins.property.mixin_imports_code.abc_fy import (
    MixinImportsCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinImportsCode_UsingFilteredMixinImports_PropertyMixin(
    # Property_mixins
    FilteredMixinImports_PropertyMixin_ABC,
    MixinImportsCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_imports_code(self) -> str:
        # fy:end <<<===
        return "\n".join(
            self._filtered_mixin_imports
            + ([""] if self._filtered_mixin_imports else [])
        )
