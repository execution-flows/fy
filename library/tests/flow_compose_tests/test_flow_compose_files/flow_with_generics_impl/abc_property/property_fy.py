# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetingT


property greeting[GreetingT]: GreetingT using greeting_message:
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.flow_with_generics_impl.abc_property.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from typing import Generic
from ..greetings_t import GreetingT


# fy:start ===>>>
class Greeting_UsingGreetingMessage_PropertyMixin(
    # Property Mixins
    Greeting_PropertyMixin_ABC[GreetingT],
    Generic[GreetingT],
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> GreetingT:
        # fy:end <<<===
        return GreetingT()
