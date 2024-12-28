# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_required_2: str using required_2:
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property2.abc_fy import (
    PropertyRequired2_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyRequired2_UsingRequired2_PropertyMixin(
    # Property_mixins
    PropertyRequired2_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_required_2(self) -> str:
        # fy:end <<<===
        return "required_2"
