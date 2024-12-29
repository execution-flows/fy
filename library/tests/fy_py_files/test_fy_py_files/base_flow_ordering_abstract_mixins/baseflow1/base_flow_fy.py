# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
@callable
base flow Ordering -> str:
    property property_required_2 using required_2
    property property_required_1 using required_1
    method method_required_1
    method method_required_2
fy"""

import abc
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method1.abc_fy import (
    MethodRequired1_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method2.abc_fy import (
    MethodRequired2_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property1.property_required_1_fy import (
    PropertyRequired1_UsingRequired1_PropertyMixin,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property2.property_required_2_fy import (
    PropertyRequired2_UsingRequired2_PropertyMixin,
)


# fy:start ===>>>
class Ordering_BaseFlow(
    # Property Mixins
    PropertyRequired2_UsingRequired2_PropertyMixin,
    PropertyRequired1_UsingRequired1_PropertyMixin,
    # Abstract Method Mixins
    MethodRequired1_MethodMixin_ABC,
    MethodRequired2_MethodMixin_ABC,
    # Base
    FlowBase[str],
    abc.ABC,
):
    def __call__(self) -> str:
        # fy:end <<<===
        return self._property_required_2 + self._property_required_1
