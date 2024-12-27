# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetT, FrenchGreeting


method greet[GreetT](greeting: str) -> int using constant:
    property french_greeting[FrenchGreeting]
"""

import abc
from fy_py_files.test_fy_py_files.method_with_generics_impl.abc_method.abc_fy import (
    Greet_MethodMixin_ABC,
)
from fy_py_files.test_fy_py_files.method_with_generics_impl.abc_property.abc_fy import (
    FrenchGreeting_PropertyMixin_ABC,
)
from typing import Generic
from .greetings_t import FrenchGreeting
from .greetings_t import GreetT


# fy:start ===>>>
class Greet_UsingConstant_MethodMixin(
    # Property_mixins
    FrenchGreeting_PropertyMixin_ABC[FrenchGreeting],
    # Method_mixins
    Greet_MethodMixin_ABC[GreetT],
    Generic[GreetT],
    abc.ABC,
):
    def _greet(self, greeting: str) -> int:
        # fy:end <<<===
        return len(greeting)
