# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetingT

property property_required_1[GreetingT]: str
fy"""

import abc
from typing import Generic
from ..greetings_t import GreetingT


# fy:start ===>>>
class PropertyRequired1_PropertyMixin_ABC(
    Generic[GreetingT],
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def _property_required_1(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
