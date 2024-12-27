# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel


flow CreateTemplateModelUsingParsedFyPyFile -> BaseTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
    property abstract_entities_ordering_index using setter
"""

from typing import Any
from typing import Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import (
    BaseTemplateModel,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from fy_library.flows.create_template_model_using_parsed_fy_py_file.abstract_method_template_model_fy import (
    CreateAbstractMethodTemplateModel_UsingParsedFyPyFile_Flow,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.abstract_property_template_model_fy import (
    CreateAbstractPropertyTemplateModel_UsingParsedFyPyFile_Flow,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.base_flow_template_model_fy import (
    CreateBaseFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.flow_template_model_fy import (
    CreateFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.method_template_model_fy import (
    CreateMethodTemplateModel_UsingParsedFyPyFile_Flow,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.property_template_model_fy import (
    CreatePropertyTemplateModel_UsingParsedFyPyFile_Flow,
)
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreateTemplateModelUsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    # Base
    FlowBase[BaseTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        abstract_entities_ordering_index: Dict[str, int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> BaseTemplateModel:
        # fy:end <<<===
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                return CreateFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                    parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                )()
            case ParsedFyPyFileKind.BASE_FLOW:
                return CreateBaseFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                    parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                    abstract_entities_ordering_index=self._abstract_entities_ordering_index,
                )()
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                return CreateAbstractPropertyTemplateModel_UsingParsedFyPyFile_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                )()
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                return CreateAbstractMethodTemplateModel_UsingParsedFyPyFile_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                )()
            case ParsedFyPyFileKind.PROPERTY:
                return CreatePropertyTemplateModel_UsingParsedFyPyFile_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                    abstract_entities_ordering_index=self._abstract_entities_ordering_index,
                )()
            case ParsedFyPyFileKind.METHOD:
                return CreateMethodTemplateModel_UsingParsedFyPyFile_Flow(
                    parsed_fy_py_file=self._parsed_fy_py_file,
                    abstract_entities_ordering_index=self._abstract_entities_ordering_index,
                )()

        raise NotImplementedError(
            f"No Template Model for {self._parsed_fy_py_file.file_type}"
        )
