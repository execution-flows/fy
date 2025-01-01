# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetingT2

method method_required_1[GreetingT2] -> str using required_1:
fy"""

import abc
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.method_required_1.abc_fy import (
    MethodRequired1_MethodMixin_ABC,
)
from typing import Generic
from ..greetings_t import GreetingT2


# fy:start ===>>>
class MethodRequired1_UsingRequired1_MethodMixin(
    # Generic Method Mixins
    MethodRequired1_MethodMixin_ABC[GreetingT2],
    Generic[GreetingT2],
    abc.ABC,
):
    def _method_required_1(self) -> str:
        # fy:end <<<===
        return "required_1"
