# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow PropertyImports -> List[str]:
    property abstract_property_mixins using setter
    property mixin_import_map using setter
    property parsed_property_fy_py_file using setter
    property cached_import using constant
    property import_generic using generic_constant
    property import_abc using when_abstract_property_mixins_exists
    property import_abstract_property_mixins using abstract_property_mixin_and_mixin_import_map
"""

from typing import List, Any, Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.mixin_models import AbstractPropertyModel
from fy_library.mixins.property.abstract_property_mixins.using_setter import (
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports.cached_import__using_constant_fy import (
    CachedImport_UsingConstant_PropertyMixin,
)
from fy_library.mixins.property.imports.import__abstract_property_mixins__using_abstract_property_mixin_and_mixin_import_map__fy import (
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports.import_abc__using_when_abstract_property_mixins_exists__fy import (
    ImportAbc_UsingWhenAbstractPropertyMixinsExists_PropertyMixin,
)
from fy_library.mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.imports.import_generic__using_generic_constant_fy import (
    ImportGeneric_UsingGenericConstant_PropertyMixin,
)

from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile
from fy_library.mixins.property.parsed_property_fy_py_file.using_setter import (
    ParsedPropertyFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class PropertyImports_Flow(
    # Property Mixins
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedPropertyFyPyFile_UsingSetter_PropertyMixin,
    CachedImport_UsingConstant_PropertyMixin,
    ImportGeneric_UsingGenericConstant_PropertyMixin,
    ImportAbc_UsingWhenAbstractPropertyMixinsExists_PropertyMixin,
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        abstract_property_mixins: List[AbstractPropertyModel],
        mixin_import_map: Dict[str, str],
        parsed_property_fy_py_file: ParsedPropertyFyPyFile,
        **kwargs: Any,
    ):
        self._abstract_property_mixins = abstract_property_mixins
        self._mixin_import_map = mixin_import_map
        self._parsed_property_fy_py_file = parsed_property_fy_py_file
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
