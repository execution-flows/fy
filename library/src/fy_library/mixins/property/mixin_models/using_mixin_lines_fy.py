# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.fy_py_template_models import BaseMixinModel


property mixin_models: List[BaseMixinModel] using mixin_lines:
    property fy_py_file_to_parse
    property mixin_lines
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.fy_py_template_models import (
    BaseMixinModel,
)
from fy_library.flows.mixin_model.mixin_lines_to_mixin_line_flow_fy import (
    MixinLinesToMixinLine_Flow,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_lines.abc_fy import (
    MixinLines_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinModels_UsingMixinLines_PropertyMixin(
    # Property_mixins
    FyPyFileToParse_PropertyMixin_ABC,
    MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_models(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        mixin_models = MixinLinesToMixinLine_Flow(
            mixin_lines=self._mixin_lines, fy_py_file_to_parse=self._fy_py_file_to_parse
        )()

        return mixin_models
