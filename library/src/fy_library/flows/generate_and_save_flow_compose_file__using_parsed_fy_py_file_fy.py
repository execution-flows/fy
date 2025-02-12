# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow generate_and_save_flow_compose_file__using_parsed_fy_py_file -> None:
    property parsed_fy_py_file using setter
    property mixin_import_map using setter
    property parsed_fy_py_files_map_by_key using setter
    property abstract_entities_ordering_index using setter
    property mixin_imports using parsed_fy_py_file
    property jinja2_template_file_name using parsed_fy_py_file
    property template_model using parsed_fy_py_file
    property flow_compose_file_content using parsed_fy_py_file
    property generated_flow_compose_code using jinja2_templates
    property flow_compose_file_name using parsed_fy_py_file
    method generate_and_save_flow_compose_code using flow_compose_file_content
fy"""

from typing import Any

from fy_core.base.flow_base import FlowBase

from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.method.generate_and_save_flow_compose_code.using_generated_flow_compose_code_fy import (
    GenerateAndSaveFlowComposeCode_UsingFlowComposeFileContent_MethodMixin,
)
from fy_library.mixins.property.flow_compose_file.flow_compose_file_name.using_parsed_fy_py_file_fy import (
    FlowComposeFileName_UsingParsedFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_imports.using_parsed_fy_py_file_fy import (
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.mro.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.templates.generated_flow_compose_code.using_jinja2_templates_fy import (
    GeneratedFlowComposeCode_UsingJinja2Templates_PropertyMixin,
)
from fy_library.mixins.property.templates.jinja2_template_file_name.using_parsed_fy_py_file_fy import (
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.templates.template_model.using_parsed_fy_py_file_fy import (
    TemplateModel_UsingParsedFyPyFile_PropertyMixin,
)

from fy_library.mixins.property.flow_compose_file.flow_compose_file_content.using_parsed_fy_py_file_fy import (
    FlowComposeFileContent_UsingParsedFyPyFile_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFlowComposeFile_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
    TemplateModel_UsingParsedFyPyFile_PropertyMixin,
    FlowComposeFileContent_UsingParsedFyPyFile_PropertyMixin,
    GeneratedFlowComposeCode_UsingJinja2Templates_PropertyMixin,
    FlowComposeFileName_UsingParsedFyPyFile_PropertyMixin,
    # Method Mixins
    GenerateAndSaveFlowComposeCode_UsingFlowComposeFileContent_MethodMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str],
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
        abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._mixin_import_map = mixin_import_map
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        self._generate_and_save_flow_compose_code()
