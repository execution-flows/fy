# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method method_required_3 -> str using required_1_2_3:
    property property_required_1
    property property_required_2
    property property_required_3
fy"""

import abc
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method3.abc_fy import (
    MethodRequired3_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property1.abc_fy import (
    PropertyRequired1_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property2.abc_fy import (
    PropertyRequired2_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.property3.abc_fy import (
    PropertyRequired3_PropertyMixin_ABC,
)


# fy:start ===>>>
class MethodRequired3_UsingRequired123_MethodMixin(
    # Property_mixins
    PropertyRequired1_PropertyMixin_ABC,
    PropertyRequired2_PropertyMixin_ABC,
    PropertyRequired3_PropertyMixin_ABC,
    # Method_mixins
    MethodRequired3_MethodMixin_ABC,
    abc.ABC,
):
    def _method_required_3(self) -> str:
        # fy:end <<<===
        return "required_2"
