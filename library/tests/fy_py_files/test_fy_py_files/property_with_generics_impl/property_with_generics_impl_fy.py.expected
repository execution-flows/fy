# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT, SpanishGreeting


property hello_world[GreetingT]: str using spanish_greeting:
    property spanish_greeting[SpanishGreeting]
"""

from functools import cached_property
import abc
from typing import Generic
from fy_py_files.test_fy_py_files.property_with_generics_impl.abc_fy import (
    SpanishGreeting_PropertyMixin_ABC,
)
from .greetings_t import GreetingT, SpanishGreeting


# fy:start ===>>>
class HelloWorld_UsingSpanishGreeting_PropertyMixin(
    # Property_mixins
    SpanishGreeting_PropertyMixin_ABC[SpanishGreeting],
    Generic[GreetingT],
    abc.ABC,
):
    @cached_property
    def _hello_world(self) -> str:
        # fy:end <<<===
        return "Hello World"
