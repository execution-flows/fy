# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreateAbstractPropertyTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels -> AbstractPropertyTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
"""

from typing import Any
from typing import Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import AbstractPropertyTemplateModel
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedAbstractPropertyFyPyFile,
)
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreateAbstractPropertyTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    # Base
    FlowBase[AbstractPropertyTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        super().__init__(*args, **kwargs)

    def __call__(self) -> AbstractPropertyTemplateModel:
        # fy:end <<<===
        parsed_abstract_property_fy_py_file = self._parsed_fy_py_file
        assert isinstance(
            parsed_abstract_property_fy_py_file, ParsedAbstractPropertyFyPyFile
        )
        return AbstractPropertyTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{parsed_abstract_property_fy_py_file.abstract_property_name.pascal_case}_PropertyMixin_ABC"
            ),
            abstract_property_name=parsed_abstract_property_fy_py_file.abstract_property_name,
            property_type=parsed_abstract_property_fy_py_file.property_type,
        )
