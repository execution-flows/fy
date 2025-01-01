# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetingT

property property_required_1[GreetingT]: str using required_1:
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.ordered_abstract_methods_test.property_required_1.abc_fy import (
    PropertyRequired1_PropertyMixin_ABC,
)
from typing import Generic
from ..greetings_t import GreetingT


# fy:start ===>>>
class PropertyRequired1_UsingRequired1_PropertyMixin(
    # Property_mixins
    PropertyRequired1_PropertyMixin_ABC[GreetingT],
    Generic[GreetingT],
    abc.ABC,
):
    @cached_property
    def _property_required_1(self) -> str:
        # fy:end <<<===
        return "required_1"
