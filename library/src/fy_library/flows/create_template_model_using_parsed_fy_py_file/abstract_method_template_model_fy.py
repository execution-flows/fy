# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreateAbstractMethodTemplateModel_UsingParsedFyPyFile -> AbstractMethodTemplateModel:
    property parsed_fy_py_file using setter
"""

from typing import Any

from fy_core.base.flow_base import FlowBase

from fy_library.domain.fy_py_template_models import AbstractMethodTemplateModel
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedAbstractMethodFyPyFile,
)
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreateAbstractMethodTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    # Base
    FlowBase[AbstractMethodTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> AbstractMethodTemplateModel:
        # fy:end <<<===
        parsed_abstract_method_fy_py_file = self._parsed_fy_py_file

        assert isinstance(
            parsed_abstract_method_fy_py_file, ParsedAbstractMethodFyPyFile
        )
        return AbstractMethodTemplateModel(
            python_class_name=parsed_abstract_method_fy_py_file.python_class_name,
            abstract_method_name=parsed_abstract_method_fy_py_file.abstract_method_name,
            generics_def=parsed_abstract_method_fy_py_file.generics_def,
            arguments=parsed_abstract_method_fy_py_file.arguments,
            return_type=parsed_abstract_method_fy_py_file.return_type,
        )
