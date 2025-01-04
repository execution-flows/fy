# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetingT2

method method_impl_2[GreetingT2] -> str using impl_2:
    property property_required_2
    property property_required_1[str]
    method method_required_2
    method method_required_1[GreetingT2]
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
from typing import Generic
from ..greetings_t import GreetingT2


# fy:start ===>>>
class MethodImpl2_UsingImpl2_MethodMixin(
    # Property Mixins
    PropertyRequired2_PropertyMixin_ABC,
    # Method Mixins
    MethodImpl2_MethodMixin_ABC,
    MethodRequired2_MethodMixin_ABC,
    # Generic Property Mixins
    PropertyRequired1_PropertyMixin_ABC[str],
    # Generic Method Mixins
    MethodRequired1_MethodMixin_ABC[GreetingT2],
    Generic[GreetingT2],
    abc.ABC,
):
    def _method_impl_2(self) -> str:
        # fy:end <<<===
        return self._property_required_2 + self._property_required_1
