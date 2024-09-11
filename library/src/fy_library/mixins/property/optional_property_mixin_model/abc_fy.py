# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.mixin_models import PropertyMixinModel


property optional_property_mixin_model: PropertyMixinModel | None
"""

import abc

from fy_library.domain.mixin_models import PropertyMixinModel


# fy:start ===>>>
class OptionalPropertyMixinModel_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _optional_property_mixin_model(self) -> PropertyMixinModel | None:
        raise NotImplementedError()
        # fy:end <<<===
