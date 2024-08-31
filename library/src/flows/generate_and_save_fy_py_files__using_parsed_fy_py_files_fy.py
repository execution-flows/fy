# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles -> None:
    property parsed_fy_py_files using setter
    property mixin_import_map using setter
    method generate_fy_py_code using jinja2_templates
"""
from typing import List, Any, Dict

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from flows.generate_and_save_fy_py_file__using_parsed_fy_py_file_fy import (
    GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow,
)
from mixins.method.generate_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
)
from mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from mixins.property.parsed_fy_py_files.using_setter import (
    ParsedFyPyFiles_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles_Flow(
    # Property Mixins
    ParsedFyPyFiles_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    # Method Mixins
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        for parsed_fy_py_file in self._parsed_fy_py_files:
            GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow(
                parsed_fy_py_file=parsed_fy_py_file,
            )

    def __init__(
        self,
        *args: Any,
        parsed_fy_py_files: List[ParsedFyPyFile],
        mixin_import_map: Dict[str, str],
        **kwargs: Any,
    ):
        self._parsed_fy_py_files = parsed_fy_py_files
        self._mixin_import_map = mixin_import_map
        super().__init__(*args, **kwargs)
