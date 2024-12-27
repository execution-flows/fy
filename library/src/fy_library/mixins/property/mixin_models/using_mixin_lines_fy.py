# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import BaseMixinModel


property mixin_models: List[BaseMixinModel] using mixin_lines:
    property fy_py_file_to_parse
    property mixin_lines
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.mixin_models import BaseMixinModel
from fy_library.flows.mixin_model.mixin_line_to_mixin_model_fy import (
    MixinLineToMixinModel_Flow,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_lines.abc_fy import (
    MixinLines_PropertyMixin_ABC,
)

from fy_library.mixins.property.mixin_models.abc_fy import (
    MixinModels_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinModels_UsingMixinLines_PropertyMixin(
    # Property_mixins
    FyPyFileToParse_PropertyMixin_ABC,
    MixinLines_PropertyMixin_ABC,
    MixinModels_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_models(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        return [
            MixinLineToMixinModel_Flow(
                mixin_line=mixin_line, fy_py_file_to_parse=self._fy_py_file_to_parse
            )()
            for mixin_line in self._mixin_lines
            if mixin_line != ""
        ]
