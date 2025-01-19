# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property import_abc: List[str] using when_abstract_property_mixins_exists:
    property abstract_property_mixins
fy"""

import abc
from functools import cached_property
from typing import List

from fy_library.mixins.property.entity_mixins.abstract_property_mixins.abc_fy import (
    AbstractPropertyMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports_and_user_imports.import_abc.abc_fy import (
    ImportAbc_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportAbc_UsingWhenAbstractPropertyMixinsExists_PropertyMixin(
    # Property Mixins
    AbstractPropertyMixins_PropertyMixin_ABC,
    ImportAbc_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_abc(self) -> List[str]:
        # fy:end <<<===
        static_imports = ["import abc"] if self._abstract_property_mixins else []
        return static_imports
