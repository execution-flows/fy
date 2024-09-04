# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property property_setter_imports: List[str] using property_mixins:
    property parsed_fy_py_files_map_by_key
    property property_mixins
"""

import abc
from functools import cached_property
from typing import List, Set

from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_mixins.abc_fy import (
    PropertyMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertySetterImports_UsingPropertyMixins_PropertyMixin(
    # Property_mixins
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_setter_imports(self) -> List[str]:
        # fy:end <<<===
        property_setters = [
            property_mixin
            for property_mixin in self._property_mixins
            if property_mixin.implementation_name.snake_case == "setter"
        ]
        user_imports_split = self._parsed_fy_py_files_map_by_key
        user_imports: Set[str] = set()
        for property_setter in property_setters:
            user_imports.update(
                [
                    user_import
                    for user_import in user_imports_split[
                        property_setter.property_name.snake_case
                    ].user_imports.split("\n")
                    if user_import != ""
                ]
            )

        return list(user_imports) if property_setters else []
