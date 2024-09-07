# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property mixin_lines: List[str] using base_flow_file_split:
    property base_flow_file_split
"""

import abc
from functools import cached_property
from typing import List

from fy_library.mixins.property.base_flow_file_split.abc_fy import (
    BaseFlowFileSplit_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinLines_UsingBaseFlowFileSplit_PropertyMixin(
    # Property_mixins
    BaseFlowFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_lines(self) -> List[str]:
        # fy:end <<<===
        return self._base_flow_file_split.mixins.split("\n")
