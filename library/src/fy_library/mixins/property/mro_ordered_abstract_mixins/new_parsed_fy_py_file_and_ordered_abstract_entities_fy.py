# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import AbstractPropertyModel


property mro_ordered_abstract_mixins: List[AbstractPropertyModel] using abstract_mixins_and_ordered_abstract_entities:
    property abstract_mixins
    property ordered_abstract_entities
"""

from functools import cached_property
from typing import List

from fy_library.domain.mixin_models import AbstractPropertyModel

import abc
from fy_library.mixins.property.abstract_mixins.abc_fy import (
    AbstractMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.ordered_abstract_entities.abc_fy import (
    OrderedAbstractEntities_PropertyMixin_ABC,
)


# fy:start ===>>>
class MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin(
    # Property_mixins
    AbstractMixins_PropertyMixin_ABC,
    OrderedAbstractEntities_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mro_ordered_abstract_mixins(self) -> List[AbstractPropertyModel]:
        # fy:end <<<===
        return sorted(
            self._abstract_mixins,
            key=lambda m: self._ordered_abstract_entities[m.property_name.snake_case],
        )
