# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import FrenchGreeting


flow setter_uses_generic_test -> None:
    property greeting using setter[FrenchGreeting]
fy"""

from ..greetings_t import GreetingT
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.flow_uses_setters_with_generics_impl.greeting.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)
from typing import Any
from .greetings_t import FrenchGreeting


# fy:start ===>>>
class SetterUsesGenericTest_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin[FrenchGreeting],
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        greeting: GreetingT,
        **kwargs: Any,
    ):
        self._greeting = greeting
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        return None
