# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import BaseMixinModel


property mro_ordered_abstract_mixins: list[BaseMixinModel] using abstract_mixins_and_ordered_abstract_entities:
    property abstract_mixins
    property abstract_entities_ordering_index
fy"""

import abc
from functools import cached_property

from fy_library.domain.mixin_models import BaseMixinModel
from fy_library.mixins.property.entity_mixins.abstract_mixins.abc_fy import (
    AbstractMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.mro.mro_ordered_abstract_mixins.abc_fy import (
    MroOrderedAbstractMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.mro.ordered_abstract_entities.abc_fy import (
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
)


# fy:start ===>>>
class MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin(
    # Property Mixins
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
    AbstractMixins_PropertyMixin_ABC,
    MroOrderedAbstractMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mro_ordered_abstract_mixins(self) -> list[BaseMixinModel]:
        # fy:end <<<===
        return sorted(
            self._abstract_mixins,
            key=lambda m: self._abstract_entities_ordering_index[m.entity_key],
        )
