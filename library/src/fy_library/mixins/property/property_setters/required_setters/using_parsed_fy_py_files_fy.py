# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property required_setters: dict[str, PropertySetterFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
    property parsed_fy_py_files_map_by_key
    property project_root_folder
fy"""

import abc
from functools import cached_property
from typing import List, cast

from fy_library.constants import (
    GENERATED_PROPERTY_FILE_IMPLEMENTATION_NAMES,
    PROPERTY_SETTER_IMPLEMENTATION_NAME,
)
from fy_library.domain.entity_key import entity_key
from fy_library.domain.fy_py_template_models import TemporaryBaseTemplateModel
from fy_library.domain.mixin_models import PropertyMixinModel
from fy_library.domain.parsed_fy_py_file import (
    PropertySetterFyPyFile,
    ParsedFyPyFile,
    ParsedAbstractPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.fy_file.project_root_folder.abc_fy import (
    ProjectRootFolder_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.required_setters.abc_fy import (
    RequiredSetters_PropertyMixin_ABC,
)


# fy:start ===>>>
class RequiredSetters_UsingParsedFyPyFiles_PropertyMixin(
    # Property Mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    ProjectRootFolder_PropertyMixin_ABC,
    RequiredSetters_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_setters(self) -> dict[str, PropertySetterFyPyFile]:
        # fy:end <<<===
        def get_properties(
            parsed_fy_py_file: ParsedFyPyFile,
        ) -> List[PropertyMixinModel]:
            assert hasattr(parsed_fy_py_file, "properties")
            return cast(List[PropertyMixinModel], parsed_fy_py_file.properties)

        def get_file_path(flow_property) -> str:
            parsed_fy_py_file_path = cast(
                ParsedAbstractPropertyFyPyFile,
                self._parsed_fy_py_files_map_by_key[
                    ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                    flow_property.property_name.snake_case,
                ],
            )
            relative_file_folder_path = (
                parsed_fy_py_file_path.file_path.parent.relative_to(
                    self._project_root_folder
                )
            )
            file_name = parsed_fy_py_file_path.file_path.stem
            python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
            return f"from {python_file_path} import (\n {' ' * 4}{parsed_fy_py_file_path.python_class_name.pascal_case}\n)"

        required_setters = {
            flow_property.property_name.snake_case: PropertySetterFyPyFile(
                pre_fy_code="",
                fy_code="",
                pre_marker_file_content="",
                post_marker_file_content="",
                file_path=self._parsed_fy_py_files_map_by_key[
                    ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                    flow_property.property_name.snake_case,
                ].file_path.with_name("using_setter.py"),
                user_imports=self._parsed_fy_py_files_map_by_key[
                    ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                    flow_property.property_name.snake_case,
                ].user_imports,
                python_class_name=flow_property.python_class_name,
                generics_def=cast(
                    ParsedAbstractPropertyFyPyFile,
                    self._parsed_fy_py_files_map_by_key[
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        flow_property.property_name.snake_case,
                    ],
                ).generics_def,
                property_type=cast(
                    ParsedAbstractPropertyFyPyFile,
                    self._parsed_fy_py_files_map_by_key[
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        flow_property.property_name.snake_case,
                    ],
                ).property_type,
                property_name=flow_property.property_name,
                implementation_name=flow_property.implementation_name,
                abstract_mixin_name=cast(
                    ParsedAbstractPropertyFyPyFile,
                    self._parsed_fy_py_files_map_by_key[
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        flow_property.property_name.snake_case,
                    ],
                ).python_class_name,
                abstract_mixin_import=get_file_path(flow_property),
                template_model=TemporaryBaseTemplateModel(
                    python_class_name=flow_property.python_class_name,
                    entity_key_value=entity_key(
                        fy_py_kind=ParsedFyPyFileKind.PROPERTY_SETTER,
                        mixin_name__snake_case=flow_property.property_name.snake_case,
                        mixin_implementation_name__snake_case=PROPERTY_SETTER_IMPLEMENTATION_NAME,
                    ),
                ),
            )
            for parsed_fy_py_file in self._parsed_fy_py_files
            if parsed_fy_py_file.file_type
            in {ParsedFyPyFileKind.FLOW, ParsedFyPyFileKind.BASE_FLOW}
            for flow_property in get_properties(parsed_fy_py_file)
            if (
                flow_property.implementation_name.snake_case
                in GENERATED_PROPERTY_FILE_IMPLEMENTATION_NAMES
                and (
                    flow_property.entity_key[0],
                    f"{flow_property.property_name.snake_case}.setter",
                )
                not in self._parsed_fy_py_files_map_by_key
            )
        }

        return required_setters
