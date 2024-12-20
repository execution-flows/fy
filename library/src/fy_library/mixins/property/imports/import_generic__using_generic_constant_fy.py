# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_generic: List[str] using generic_constant:
"""

from functools import cached_property
from typing import List


# fy:start ===>>>
class ImportGeneric_UsingGenericConstant_PropertyMixin:
    @cached_property
    def _import_generic(self) -> List[str]:
        # fy:end <<<===
        return [
            # static import
            "from typing import Generic"
        ]
