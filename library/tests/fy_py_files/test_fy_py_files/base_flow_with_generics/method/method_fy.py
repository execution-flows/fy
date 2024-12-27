# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetT


method greet[GreetT](message: str) -> str using greeting:
"""

import abc
from fy_py_files.test_fy_py_files.base_flow_with_generics.method.abc_fy import (
    Greet_MethodMixin_ABC,
)
from typing import Generic
from ..greetings_t import GreetT


# fy:start ===>>>
class Greet_UsingGreeting_MethodMixin(
    # Method_mixins
    Greet_MethodMixin_ABC[GreetT],
    Generic[GreetT],
    abc.ABC,
):
    def _greet(self, message: str) -> str:
        # fy:end <<<===
        return message
