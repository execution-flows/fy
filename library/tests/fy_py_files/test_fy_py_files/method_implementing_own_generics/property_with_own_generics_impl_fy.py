# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import SpanishGreeting, GreetingT


method greet -> SpanishGreeting using spanish_greeting:
    method greet[GreetingT]
fy"""

import abc
from fy_py_files.test_fy_py_files.method_implementing_own_generics.abc_fy import (
    Greet_MethodMixin_ABC,
)
from .greetings_t import GreetingT
from .greetings_t import SpanishGreeting


# fy:start ===>>>
class Greet_UsingSpanishGreeting_MethodMixin(
    # Method_mixins
    Greet_MethodMixin_ABC[GreetingT],
    abc.ABC,
):
    def _greet(self) -> SpanishGreeting:
        # fy:end <<<===
        return SpanishGreeting()
