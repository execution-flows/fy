# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters -> None:
    property required_property_setters_fy_py using setter
"""

from typing import Any, List

from fy_core.base.flow_base import FlowBase

from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile
from fy_library.flows.generate_and_save_fy_py_file__using_required_property_setters_fy import (
    GenerateAndSaveFyPyFile_UsingRequiredPropertySetters_Flow,
)
from fy_library.mixins.property.required_property_setters_fy_py.using_setter import (
    RequiredPropertySettersFyPy_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow(
    # Property Mixins
    RequiredPropertySettersFyPy_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        required_property_setters_fy_py: List[PropertySetterFyPyFile],
        **kwargs: Any,
    ):
        self._required_property_setters_fy_py = required_property_setters_fy_py
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        for parsed_fy_py_file in self._required_property_setters_fy_py:
            GenerateAndSaveFyPyFile_UsingRequiredPropertySetters_Flow(
                parsed_fy_py_file=parsed_fy_py_file,
            )()
