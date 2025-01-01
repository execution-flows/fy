# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method method_impl_2 -> str using impl_2:
    property property_required_2
    property property_required_1[str]
    method method_required_2
    method method_required_1[str]
fy"""

import abc
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method_impl_2.abc_fy import (
    MethodImpl2_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method_required_1.abc_fy import (
    MethodRequired1_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method_required_2.abc_fy import (
    MethodRequired2_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.property_required_1.abc_fy import (
    PropertyRequired1_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.property_required_2.abc_fy import (
    PropertyRequired2_PropertyMixin_ABC,
)


# fy:start ===>>>
class MethodImpl2_UsingImpl2_MethodMixin(
    # Property_mixins
    PropertyRequired2_PropertyMixin_ABC,
    # Method_mixins
    MethodImpl2_MethodMixin_ABC,
    MethodRequired2_MethodMixin_ABC,
    # Generic Property Mixins
    PropertyRequired1_PropertyMixin_ABC[str],
    # Generic Method Mixins
    MethodRequired1_MethodMixin_ABC[str],
    abc.ABC,
):
    def _method_impl_2(self) -> str:
        # fy:end <<<===
        return self._property_required_2 + self._property_required_1
