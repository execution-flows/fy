# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_abc: List[str] using when_abstract_property_and_abstract_method_exists:
    property abstract_property_mixins
    property abstract_method_mixins
fy"""

import abc
from functools import cached_property
from typing import List

from fy_library.mixins.property.entity_mixins.abstract_method_mixins.abc_fy import (
    AbstractMethodMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.entity_mixins.abstract_property_mixins.abc_fy import (
    AbstractPropertyMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports_and_user_imports.import_abc.abc_fy import (
    ImportAbc_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportAbc_UsingWhenAbstractPropertyAndAbstractMethodExists_PropertyMixin(
    # Property Mixins
    AbstractMethodMixins_PropertyMixin_ABC,
    AbstractPropertyMixins_PropertyMixin_ABC,
    ImportAbc_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_abc(self) -> List[str]:
        # fy:end <<<===
        return (
            ["import abc"]
            if (self._abstract_property_mixins or self._abstract_method_mixins)
            else []
        )
