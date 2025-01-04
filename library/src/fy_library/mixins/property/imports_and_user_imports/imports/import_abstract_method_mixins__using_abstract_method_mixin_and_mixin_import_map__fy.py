# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property import_abstract_method_mixins: list[str] using abstract_method_mixin_and_mixin_import_map:
    property mixin_import_map
    property abstract_method_mixins
fy"""

import abc
from functools import cached_property

from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.entity_mixins.abstract_method_mixins.abc_fy import (
    AbstractMethodMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class ImportAbstractMethodMixins_UsingAbstractMethodMixinAndMixinImportMap_PropertyMixin(
    # Property Mixins
    AbstractMethodMixins_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _import_abstract_method_mixins(self) -> list[str]:
        # fy:end <<<===
        return [
            # method mixins
            self._mixin_import_map[
                ParsedFyPyFileKind(abstract_method_mixin.kind.value),
                abstract_method_mixin.method_name.snake_case,
            ]
            for abstract_method_mixin in self._abstract_method_mixins
        ]
