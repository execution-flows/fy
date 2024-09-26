# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreatePropertyTemplateModel_UsingParsedFyPyFile -> PropertyTemplateModel:
    property parsed_fy_py_file using setter
"""

from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import PropertyTemplateModel
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedPropertyFyPyFile
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreatePropertyTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    # Base
    FlowBase[PropertyTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> PropertyTemplateModel:
        # fy:end <<<===
        parsed_property_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_property_fy_py_file, ParsedPropertyFyPyFile)
        return PropertyTemplateModel(
            python_class_name=parsed_property_fy_py_file.python_class_name,
            property_name=parsed_property_fy_py_file.property_name,
            implementation_name=parsed_property_fy_py_file.implementation_name,
            abstract_property_mixins=parsed_property_fy_py_file.abstract_property_mixins,
            property_type=parsed_property_fy_py_file.property_type,
        )
