# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow property_imports -> List[str]:
    property abstract_property_mixins using setter
    property mixin_import_map using setter
    property parsed_property_fy_py_file using setter
    property cached_import using constant(["from functools import cached_property"])
    property import_generic using constant(["from typing import Generic"])
    property import_abc using when_abstract_property_mixins_exists
    property import_abstract_property_mixins using abstract_property_mixin_and_mixin_import_map
fy"""

from typing import List, Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.mixin_models import AbstractPropertyModel
from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.entity_mixins.abstract_property_mixins.using_setter import (
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.cached_import.using_setter import (
    CachedImport_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.import_generic.using_setter import (
    ImportGeneric_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.import__abstract_property_mixins__using_abstract_property_mixin_and_mixin_import_map__fy import (
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.import_abc__using_when_abstract_property_mixins_exists__fy import (
    ImportAbc_UsingWhenAbstractPropertyMixinsExists_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_property_fy_py_file.using_setter import (
    ParsedPropertyFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class PropertyImports_Flow(
    # Property Mixins
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedPropertyFyPyFile_UsingSetter_PropertyMixin,
    CachedImport_UsingSetter_PropertyMixin,
    ImportGeneric_UsingSetter_PropertyMixin,
    ImportAbc_UsingWhenAbstractPropertyMixinsExists_PropertyMixin,
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        abstract_property_mixins: List[AbstractPropertyModel],
        mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str],
        parsed_property_fy_py_file: ParsedPropertyFyPyFile,
        **kwargs: Any,
    ):
        self._abstract_property_mixins = abstract_property_mixins
        self._mixin_import_map = mixin_import_map
        self._parsed_property_fy_py_file = parsed_property_fy_py_file
        self._cached_import = ["from functools import cached_property"]
        self._import_generic = ["from typing import Generic"]
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        property_imports = (
            self._import_generic
            if self._parsed_property_fy_py_file.generics_def != ""
            else []
        )

        return (
            self._cached_import
            + self._import_abc
            + property_imports
            + self._import_abstract_property_mixins
        )
