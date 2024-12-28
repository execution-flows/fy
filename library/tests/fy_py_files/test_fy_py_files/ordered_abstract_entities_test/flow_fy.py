# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow Message -> str:
    property property_required_1 using required_1
    property property_required_2 using required_2
    property property_impl_1 using impl_1
    property property_impl_2 using impl_2
fy"""

from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property1.property_required_1_fy import (
    PropertyRequired1_UsingRequired1_PropertyMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property2.property_required_2_fy import (
    PropertyRequired2_UsingRequired2_PropertyMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property3.property_impl_1_fy import (
    PropertyImpl1_UsingImpl1_PropertyMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property4.property_impl_2_fy import (
    PropertyImpl2_UsingImpl2_PropertyMixin,
)


# fy:start ===>>>
class Message_Flow(
    # Property Mixins
    PropertyRequired1_UsingRequired1_PropertyMixin,
    PropertyRequired2_UsingRequired2_PropertyMixin,
    PropertyImpl1_UsingImpl1_PropertyMixin,
    PropertyImpl2_UsingImpl2_PropertyMixin,
    # Base
    FlowBase[str],
):
    def __call__(self) -> str:
        # fy:end <<<===
        return self._property_impl_1 + self._property_impl_2
