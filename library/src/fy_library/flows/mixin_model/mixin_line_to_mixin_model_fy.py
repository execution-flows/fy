# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow MixinLineToMixinModel -> BaseMixinModel:
    property mixin_line using setter
    property fy_py_file_to_parse using setter
    property optional_property_mixin_model using mixin_line
    property optional_method_mixin_model using mixin_line
    property optional_abstract_property_mixin_model using mixin_line
    property optional_abstract_method_mixin_model using mixin_line
"""

from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.mixin_models import BaseMixinModel
from fy_library.mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mixin_line.using_setter import (
    MixinLine_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.optional_abstract_property_mixin_model.using_mixin_line_fy import (
    OptionalAbstractPropertyMixinModel_UsingMixinLine_PropertyMixin,
)
from fy_library.mixins.property.optional_method_mixin_model.using_mixin_line_fy import (
    OptionalMethodMixinModel_UsingMixinLine_PropertyMixin,
)
from fy_library.mixins.property.optional_property_mixin_model.using_mixin_line_fy import (
    OptionalPropertyMixinModel_UsingMixinLine_PropertyMixin,
)

from fy_library.mixins.property.optional_abstract_method_mixin_model.using_mixin_line_fy import (
    OptionalAbstractMethodMixinModel_UsingMixinLine_PropertyMixin,
)


# fy:start ===>>>
class MixinLineToMixinModel_Flow(
    # Property Mixins
    MixinLine_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    OptionalPropertyMixinModel_UsingMixinLine_PropertyMixin,
    OptionalMethodMixinModel_UsingMixinLine_PropertyMixin,
    OptionalAbstractPropertyMixinModel_UsingMixinLine_PropertyMixin,
    OptionalAbstractMethodMixinModel_UsingMixinLine_PropertyMixin,
    # Base
    FlowBase[BaseMixinModel],
):
    def __init__(
        self,
        *args: Any,
        mixin_line: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._mixin_line = mixin_line
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> BaseMixinModel:
        # fy:end <<<===
        mixin_model = (
            self._optional_property_mixin_model
            or self._optional_method_mixin_model
            or self._optional_abstract_property_mixin_model
            or self._optional_abstract_method_mixin_model
        )

        if mixin_model is None:
            raise ValueError(
                f"Line {self._mixin_line} in {self._fy_py_file_to_parse} is invalid."
            )
        return mixin_model
