# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property mixin_lines: List[str] using property_file_split:
    property property_file_split
"""

import abc
from functools import cached_property
from typing import List

from fy_library.mixins.property.property_file_split.abc_fy import (
    PropertyFileSplit_PropertyMixin_ABC,
)

from fy_library.mixins.property.mixin_lines.abc_fy import (
    MixinLines_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinLines_UsingPropertyFileSplit_PropertyMixin(
    # Property_mixins
    MixinLines_PropertyMixin_ABC,
    PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_lines(self) -> List[str]:
        # fy:end <<<===
        return self._property_file_split.mixins.split("\n")
