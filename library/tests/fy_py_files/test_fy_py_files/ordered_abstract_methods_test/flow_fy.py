# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow Message -> str:
    property property_required_2 using required_2
    property property_required_1 using required_1
    method method_impl_1 using impl_1
    method method_impl_2 using impl_2
    method method_required_1 using required_1
    method method_required_2 using required_2
"""

from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method1.method_required_1_fy import (
    MethodRequired1_UsingRequired1_MethodMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method2.method_required_2_fy import (
    MethodRequired2_UsingRequired2_MethodMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method3.method_impl_1_fy import (
    MethodImpl1_UsingImpl1_MethodMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method4.method_impl_2_fy import (
    MethodImpl2_UsingImpl2_MethodMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.property1.property_required_1_fy import (
    PropertyRequired1_UsingRequired1_PropertyMixin,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.property2.property_required_2_fy import (
    PropertyRequired2_UsingRequired2_PropertyMixin,
)


# fy:start ===>>>
class Message_Flow(
    # Property Mixins
    PropertyRequired2_UsingRequired2_PropertyMixin,
    PropertyRequired1_UsingRequired1_PropertyMixin,
    # Method Mixins
    MethodImpl1_UsingImpl1_MethodMixin,
    MethodImpl2_UsingImpl2_MethodMixin,
    MethodRequired1_UsingRequired1_MethodMixin,
    MethodRequired2_UsingRequired2_MethodMixin,
    # Base
    FlowBase[str],
):
    def __call__(self) -> str:
        # fy:end <<<===
        return (
            self._method_impl_1()
            + self._method_impl_2()
            + self._property_required_1
            + self._property_required_2
        )
