# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property user_imports_from_mixins: list[str] using property_setter_mixins:
    property parsed_fy_py_files_map_by_key
    property property_setter_mixins
fy"""

import abc
from functools import cached_property
from typing import Set

from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.property_setter_mixins.abc_fy import (
    PropertySetterMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin(
    # Property Mixins
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    PropertySetterMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _user_imports_from_mixins(self) -> list[str]:
        # fy:end <<<===
        user_imports_split = self._parsed_fy_py_files_map_by_key
        user_imports: Set[str] = set()
        for property_setter in self._property_setter_mixins:
            if property_setter.generics_impl != "":
                # Generic property setters that have generics_impl
                # will have an import defined in the flow.
                continue
            user_imports.update(
                [
                    user_import
                    for user_import in user_imports_split[
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        property_setter.property_name.snake_case,
                    ].user_imports.split("\n")
                    if user_import != ""
                ]
            )

        return list(user_imports)
