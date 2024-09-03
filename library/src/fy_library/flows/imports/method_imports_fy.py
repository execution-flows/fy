# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow MethodImports -> List[str]:
    property abstract_property_mixins using setter
    property abstract_method_mixins using setter
    property mixin_import_map using setter
    property import_abc using when_abstract_property_and_abstract_method_exists
    property import_property_mixins using for_abstract_property_mixin
    property import_method_mixins using for_abstract_method_mixin
"""

from typing import Any, Dict
from typing import List

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import (
    AbstractPropertyModel,
    AbstractMethodModel,
)
from fy_library.mixins.property.abstract_method_mixins.using_setter import (
    AbstractMethodMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.abstract_property_mixins.using_setter import (
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports.import_abc__using_when_abstract_property_and_abstract_method_exists__fy import (
    ImportAbc_UsingWhenAbstractPropertyAndAbstractMethodExists_PropertyMixin,
)
from fy_library.mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)


from fy_library.mixins.property.imports.import_mixins__using_for_abstract_method_mixin__fy import (
    ImportMethodMixins_UsingForAbstractMethodMixin_PropertyMixin,
)
from fy_library.mixins.property.imports.import_mixins__using_for_abstract_property_mixin__fy import (
    ImportPropertyMixins_UsingForAbstractPropertyMixin_PropertyMixin,
)


# fy:start ===>>>
class MethodImports_Flow(
    # Property Mixins
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
    AbstractMethodMixins_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ImportAbc_UsingWhenAbstractPropertyAndAbstractMethodExists_PropertyMixin,
    ImportPropertyMixins_UsingForAbstractPropertyMixin_PropertyMixin,
    ImportMethodMixins_UsingForAbstractMethodMixin_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        abstract_property_mixins: List[AbstractPropertyModel],
        abstract_method_mixins: List[AbstractMethodModel],
        mixin_import_map: Dict[str, str],
        **kwargs: Any,
    ):
        self._abstract_property_mixins = abstract_property_mixins
        self._abstract_method_mixins = abstract_method_mixins
        self._mixin_import_map = mixin_import_map
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        return (
            self._import_abc + self._import_method_mixins + self._import_property_mixins
        )
