# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import PropertyMixinModel


property property_mixins: List[PropertyMixinModel] using template_model_properties:
    property parsed_fy_py_file
"""

from functools import cached_property
from typing import List

from fy_library.domain.mixin_models import PropertyMixinModel

from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
import abc

from fy_library.mixins.property.property_mixins.abc_fy import (
    PropertyMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyMixins_UsingTemplateModelProperties_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_mixins(self) -> List[PropertyMixinModel]:
        # fy:end <<<===
        assert hasattr(self._parsed_fy_py_file, "properties")

        return self._parsed_fy_py_file.properties
