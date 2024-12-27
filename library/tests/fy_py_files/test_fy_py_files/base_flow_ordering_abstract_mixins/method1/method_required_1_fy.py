# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method method_required_1 -> str using required_1:
"""

import abc
from fy_py_files.test_fy_py_files.base_flow_ordering_abstract_mixins.method1.abc_fy import (
    MethodRequired1_MethodMixin_ABC,
)


# fy:start ===>>>
class MethodRequired1_UsingRequired1_MethodMixin(
    # Method_mixins
    MethodRequired1_MethodMixin_ABC,
    abc.ABC,
):
    def _method_required_1(self) -> str:
        # fy:end <<<===
        return "required_1"
