# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import BaseMixinModel


property mro_ordered_abstract_mixins: List[BaseMixinModel] using abstract_mixins_and_ordered_abstract_entities:
    property abstract_mixins
    property abstract_entities_ordering_index
"""

from functools import cached_property
from typing import List

from fy_library.domain.mixin_models import BaseMixinModel

import abc
from fy_library.mixins.property.abstract_mixins.abc_fy import (
    AbstractMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.ordered_abstract_entities.abc_fy import (
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
)

from fy_library.mixins.property.mro_ordered_abstract_mixins.abc_fy import (
    MroOrderedAbstractMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin(
    # Property_mixins
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
    AbstractMixins_PropertyMixin_ABC,
    MroOrderedAbstractMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mro_ordered_abstract_mixins(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        return sorted(
            self._abstract_mixins,
            key=lambda m: self._abstract_entities_ordering_index[m.entity_key],
        )
