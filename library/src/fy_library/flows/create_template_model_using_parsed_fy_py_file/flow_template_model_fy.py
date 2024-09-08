# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters


flow CreateFlowTemplateModelWithPropertySetters_UsingParsedFyPyFileAndPropertySettersTemplateModels -> FlowTemplateModelWithPropertySetters:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
    property property_mixins using template_model_properties
    property property_setter_mixins using property_mixins
    property parsed_fy_py_files using property_setter_mixins__mapped_to_abstract_property
    property template_models using parsed_fy_py_files__with_property_setters
"""

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFlowFyPyFile
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files.using_property_setter_mixins__mapped_to_abstract_property__fy import (
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_mixins.using_template_model_properties_fy import (
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
)
from fy_library.mixins.property.property_setter_mixins.using_property_mixin_fy import (
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
)
from fy_library.mixins.property.template_models.using_parsed_fy_py_files__with_property_setters__fy import (
    TemplateModels_UsingParsedFyPyFiles_WithPropertySetters_PropertyMixin,
)
from typing import Any
from typing import Dict

from fy_library.domain.fy_py_template_models import FlowTemplateModelWithPropertySetters


# fy:start ===>>>
class CreateFlowTemplateModelWithPropertySetters_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
    TemplateModels_UsingParsedFyPyFiles_WithPropertySetters_PropertyMixin,
    # Base
    FlowBase[FlowTemplateModelWithPropertySetters],
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

    def __call__(self) -> FlowTemplateModelWithPropertySetters:
        # fy:end <<<===
        parsed_flow_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_flow_fy_py_file, ParsedFlowFyPyFile)
        return FlowTemplateModelWithPropertySetters(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{parsed_flow_fy_py_file.flow_name.pascal_case}_Flow"
            ),
            flow_name=parsed_flow_fy_py_file.flow_name,
            return_type=parsed_flow_fy_py_file.return_type,
            properties=parsed_flow_fy_py_file.properties,
            methods=parsed_flow_fy_py_file.methods,
            property_setters=self._template_models,
        )
