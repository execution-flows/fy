# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_generic: List[str] using generic_constant:
"""

from functools import cached_property
from typing import List

import abc
from fy_library.mixins.property.imports.import_generic__abc_fy import (
    ImportGeneric_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportGeneric_UsingGenericConstant_PropertyMixin(
    # Property_mixins
    ImportGeneric_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_generic(self) -> List[str]:
        # fy:end <<<===
        return [
            # static import
            "from typing import Generic"
        ]
