# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.fy_py_template_models import BaseMixinModel


flow MixinLinesToMixinLine -> List[BaseMixinModel]:
    property mixin_lines using setter
    property fy_py_file_to_parse using setter
"""

from pathlib import Path
from typing import List, Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import BaseMixinModel
from fy_library.flows.mixin_model.mixin_line_to_mixin_models_fy import (
    MixinLineToMixinModels_Flow,
)
from fy_library.mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mixin_lines.using_setter import (
    MixinLines_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class MixinLinesToMixinLine_Flow(
    # Property Mixins
    MixinLines_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    # Base
    FlowBase[List[BaseMixinModel]],
):
    def __init__(
        self,
        *args: Any,
        mixin_lines: List[str],
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._mixin_lines = mixin_lines
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        mixin_models: List[BaseMixinModel] = []
        for mixin_line in self._mixin_lines:
            if mixin_line == "":
                continue
            mixin_models.append(
                MixinLineToMixinModels_Flow(
                    mixin_line=mixin_line, fy_py_file_to_parse=self._fy_py_file_to_parse
                )()
            )
        return mixin_models
