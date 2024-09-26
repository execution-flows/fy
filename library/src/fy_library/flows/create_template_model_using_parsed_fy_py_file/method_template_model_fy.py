# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreateMethodTemplateModel_UsingParsedFyPyFile -> MethodTemplateModel:
    property parsed_fy_py_file using setter
"""

from fy_library.domain.fy_py_template_models import MethodTemplateModel
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedMethodFyPyFile
from typing import Any
from fy_core.base.flow_base import FlowBase
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreateMethodTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    # Base
    FlowBase[MethodTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> MethodTemplateModel:
        # fy:end <<<===
        parsed_method_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_method_fy_py_file, ParsedMethodFyPyFile)
        return MethodTemplateModel(
            python_class_name=parsed_method_fy_py_file.python_class_name,
            method_name=parsed_method_fy_py_file.method_name,
            implementation_name=parsed_method_fy_py_file.implementation_name,
            abstract_method_mixins=parsed_method_fy_py_file.abstract_method_mixins,
            abstract_property_mixins=parsed_method_fy_py_file.abstract_property_mixins,
            arguments=parsed_method_fy_py_file.arguments,
            return_type=parsed_method_fy_py_file.return_type,
        )
