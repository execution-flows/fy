# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT, FrenchGreeting, Greet


flow HelloWorld[GreetingT] -> None:
    property greeting using greeting_message[FrenchGreeting]
    method greet using greeting[Greet]
"""

from fy_core.base.flow_base import FlowBase
from typing import Generic
from fy_py_files.test_fy_py_files.flow_with_generics_impl.abc_property.property_fy import (
    Greeting_UsingGreetingMessage_PropertyMixin,
)
from fy_py_files.test_fy_py_files.flow_with_generics_impl.method.method_fy import (
    Greet_UsingGreeting_MethodMixin,
)
from .greetings_t import GreetingT, FrenchGreeting, Greet


# fy:start ===>>>
class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingGreetingMessage_PropertyMixin[FrenchGreeting],
    # Method Mixins
    Greet_UsingGreeting_MethodMixin[Greet],
    # Base
    FlowBase[None],
    Generic[GreetingT],
):
    def __call__(self) -> None:
        # fy:end <<<===
        return None
