# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greeting_t import GreetingT


property abstract_property_with_generics[GreetingT]: GreetingT
fy"""

import abc
from typing import Generic
from .greeting_t import GreetingT


# fy:start ===>>>
class AbstractPropertyWithGenerics_PropertyMixin_ABC(
    Generic[GreetingT],
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def _abstract_property_with_generics(self) -> GreetingT:
        raise NotImplementedError()
        # fy:end <<<===
