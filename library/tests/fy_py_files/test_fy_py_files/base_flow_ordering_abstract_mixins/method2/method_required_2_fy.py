# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method method_required_2 -> str using required_2:
fy"""

import abc
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method2.abc_fy import (
    MethodRequired2_MethodMixin_ABC,
)


# fy:start ===>>>
class MethodRequired2_UsingRequired2_MethodMixin(
    # Method Mixins
    MethodRequired2_MethodMixin_ABC,
    abc.ABC,
):
    def _method_required_2(self) -> str:
        # fy:end <<<===
        return "required_2"
