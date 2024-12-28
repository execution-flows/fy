# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT, Greet


base flow HelloWorld[GreetingT] -> None:
    property greeting using greeting_message[GreetingT]
    property greeting[GreetingT]
    method greet using greeting[Greet]
    method greet[Greet]
fy"""

import abc
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.base_flow_with_generics.method.abc_fy import (
    Greet_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_with_generics.method.method_fy import (
    Greet_UsingGreeting_MethodMixin,
)
from fy_py_files.test_fy_py_files.base_flow_with_generics.property.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_with_generics.property.property_fy import (
    Greeting_UsingGreetingMessage_PropertyMixin,
)
from typing import Generic
from .greetings_t import Greet
from .greetings_t import GreetingT


# fy:start ===>>>
class HelloWorld_BaseFlow(
    # Property Mixins
    Greeting_UsingGreetingMessage_PropertyMixin[GreetingT],
    # Method Mixins
    Greet_UsingGreeting_MethodMixin[Greet],
    # Abstract Property Mixins
    Greeting_PropertyMixin_ABC[GreetingT],
    # Abstract Method Mixins
    Greet_MethodMixin_ABC[Greet],
    # Base
    FlowBase[None],
    Generic[GreetingT],
    abc.ABC,
):
    pass
    # fy:end <<<===
