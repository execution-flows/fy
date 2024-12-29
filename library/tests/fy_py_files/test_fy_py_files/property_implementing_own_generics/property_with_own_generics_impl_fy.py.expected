# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import SpanishGreeting, GreetingT


property greeting: SpanishGreeting using spanish_greeting:
    property greeting[GreetingT]
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.property_implementing_own_generics.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from .greetings_t import GreetingT
from .greetings_t import SpanishGreeting


# fy:start ===>>>
class Greeting_UsingSpanishGreeting_PropertyMixin(
    # Property_mixins
    Greeting_PropertyMixin_ABC[GreetingT],
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> SpanishGreeting:
        # fy:end <<<===
        return SpanishGreeting()
