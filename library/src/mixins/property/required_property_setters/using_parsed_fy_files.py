from functools import cached_property

import abc

from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC
from mixins.property.parse_fy_files_map_by_key.abc import (
    With_ParseFyFilesMapByKey_PropertyMixin_ABC,
)

from domain.python_entity_name import PythonEntityName

from typing import List, cast

from domain.parsed_fy_file import (
    ParsedFyFile,
    ParsedFyFileKind,
    ParsedFlowFyFile,
    PropertySetterFyFile,
)
from domain.template_models import (
    AbstractPropertyTemplateModel,
    PropertySetterTemplateModel,
)


class RequiredPropertySetters_UsingParsedFyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyFiles_PropertyMixin_ABC,
    With_ParseFyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_property_setters(self) -> List[ParsedFyFile]:
        required_setters = {
            flow_property.property_name.snake_case: PropertySetterFyFile(
                input_fy_file_path=self._parse_fy_files_map_by_key[
                    flow_property.property_name.snake_case
                ].input_fy_file_path,
                output_py_file_path=self._parse_fy_files_map_by_key[
                    flow_property.property_name.snake_case
                ].input_fy_file_path.with_name("using_setter.py"),
                template_model=PropertySetterTemplateModel(
                    property_name=flow_property.property_name,
                    user_imports=cast(
                        AbstractPropertyTemplateModel,
                        self._parse_fy_files_map_by_key[
                            flow_property.property_name.snake_case
                        ].template_model,
                    ).user_imports,
                    python_class_name=PythonEntityName.from_pascal_case(
                        f"{flow_property.property_name.pascal_case}_UsingSetter_PropertyMixin"
                    ),
                    abstract_property_name=flow_property.property_name.snake_case,
                    return_type=cast(
                        AbstractPropertyTemplateModel,
                        self._parse_fy_files_map_by_key[
                            flow_property.property_name.snake_case
                        ].template_model,
                    ).return_type,
                ),
            )
            for parsed_fy_file in self._parsed_fy_files
            if parsed_fy_file.file_type == ParsedFyFileKind.FLOW
            for flow_property in cast(
                ParsedFlowFyFile, parsed_fy_file
            ).template_model.properties
            if (
                flow_property.implementation_name.snake_case == "setter"
                and f"{flow_property.property_name.snake_case}.setter"
                not in self._parse_fy_files_map_by_key
            )
        }
        return list(required_setters.values())
