from typing import Dict, cast

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind
from domain.template_models import (
    PropertyTemplateModel,
    FlowTemplateModel,
    AbstractPropertyTemplateModel,
    MethodTemplateModel,
    AbstractMethodTemplateModel,
)


property mixin_import_map using parsed_fy_files:

    @cached
    def -> Dict[str, str]:
        mixin_import_map = {
            self.__parsed_file_key(parsed_fy_file): self.__parsed_file_python_import(
                parsed_fy_file
            )
            for parsed_fy_file in self._parsed_fy_files
        }
        return mixin_import_map

    def __parsed_file_key(self, parsed_fy_file: ParsedFyFile) -> str:
        match parsed_fy_file.file_type:
            case ParsedFyFileKind.PROPERTY:
                property_template_model = cast(
                    PropertyTemplateModel, parsed_fy_file.template_model
                )
                return mixin_key(
                    mixin_name__snake_case=property_template_model.property_name.snake_case,
                    mixin_implementation_name__snake_case=property_template_model.implementation_name.snake_case,
                )
            case ParsedFyFileKind.METHOD:
                method_template_model = cast(
                    MethodTemplateModel, parsed_fy_file.template_model
                )
                return mixin_key(
                    mixin_name__snake_case=method_template_model.method_name.snake_case,
                    mixin_implementation_name__snake_case=method_template_model.implementation_name.snake_case,
                )
            case ParsedFyFileKind.FLOW:
                flow_template_model = cast(
                    FlowTemplateModel, parsed_fy_file.template_model
                )
                return flow_template_model.flow_name.snake_case
            case ParsedFyFileKind.ABSTRACT_PROPERTY:
                abstract_property_template_model = cast(
                    AbstractPropertyTemplateModel, parsed_fy_file.template_model
                )
                return (
                    abstract_property_template_model.abstract_property_name.snake_case
                )
            case ParsedFyFileKind.ABSTRACT_METHOD:
                abstract_method_template_model = cast(
                    AbstractMethodTemplateModel, parsed_fy_file.template_model
                )
                return abstract_method_template_model.abstract_method_name.snake_case
            case _:
                raise NotImplementedError(
                    f"Unimplemented file type: {parsed_fy_file.file_type}"
                )

    def __parsed_file_python_import(self, parsed_fy_file: ParsedFyFile) -> str:
        relative_file_folder_path = (
            parsed_fy_file.input_fy_file_path.parent.relative_to(
                self._project_root_folder
            )
        )
        file_name = parsed_fy_file.input_fy_file_path.stem
        python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
        return f"from {python_file_path} import {parsed_fy_file.template_model.python_class_name.pascal_case}"

def mixin_key(
    mixin_name__snake_case: str, mixin_implementation_name__snake_case: str
) -> str:
    return f"{mixin_name__snake_case}.{mixin_implementation_name__snake_case}"
