# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow message(ordering) -> str:
    property property_required_1 using required_1
    property property_required_2 using required_2
    method method_required_1 using required_1
    method method_required_2 using required_2
fy"""

from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.baseflow1.base_flow_fy import (
    Ordering_BaseFlow,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method1.method_required_1_fy import (
    MethodRequired1_UsingRequired1_MethodMixin,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method2.method_required_2_fy import (
    MethodRequired2_UsingRequired2_MethodMixin,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property1.property_required_1_fy import (
    PropertyRequired1_UsingRequired1_PropertyMixin,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property2.property_required_2_fy import (
    PropertyRequired2_UsingRequired2_PropertyMixin,
)


# fy:start ===>>>
class Message_Flow(
    # Property Mixins
    PropertyRequired1_UsingRequired1_PropertyMixin,
    PropertyRequired2_UsingRequired2_PropertyMixin,
    # Method Mixins
    MethodRequired1_UsingRequired1_MethodMixin,
    MethodRequired2_UsingRequired2_MethodMixin,
    # Base
    Ordering_BaseFlow,
):
    def __call__(self) -> str:
        # fy:end <<<===
        return (
            self._method_required_1()
            + self._method_required_2()
            + self._property_required_1
            + self._property_required_2
        )
