import abc
from functools import cached_property
from pathlib import Path
from typing import Dict, cast

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind
from domain.template_models import PropertyTemplateModel, FlowTemplateModel, AbstractPropertyTemplateModel
from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC


def parsed_file_key(parsed_fy_file: ParsedFyFile) -> str:
    match parsed_fy_file.file_type:
        case ParsedFyFileKind.PROPERTY:
            property_template_model = cast(PropertyTemplateModel, parsed_fy_file.template_model)
            return (f"{property_template_model.property_name.snake_case}."
                    f"{property_template_model.implementation_name.snake_case}")
        case ParsedFyFileKind.FLOW:
            flow_template_model = cast(FlowTemplateModel, parsed_fy_file.template_model)
            return flow_template_model.flow_name.snake_case
        case ParsedFyFileKind.ABSTRACT_PROPERTY:
            abstract_property_template_model = cast(AbstractPropertyTemplateModel, parsed_fy_file.template_model)
            return abstract_property_template_model.property_name.snake_case
        case _:
            raise NotImplementedError(f"Unimplemented file type: f{parsed_fy_file.file_type}")


def parsed_file_python_import(parsed_fy_file: ParsedFyFile) -> str:
    relative_file_path = parsed_fy_file.input_fy_file_path.parent.relative_to(Path.cwd())
    python_file_path = ".".join(relative_file_path.parts)
    return f"from {python_file_path} import {parsed_fy_file.template_model.python_class_name.pascal_case}"


class MixinImportMap_UsingParsedFyFiles_PropertyMixin(
    With_ParsedFyFiles_PropertyMixin_ABC,
    abc.ABC
):
    @cached_property
    def _mixin_import_map(self) -> Dict[str, str]:
        mixin_import_map = {
            parsed_file_key(parsed_fy_file): parsed_file_python_import(parsed_fy_file)
            for parsed_fy_file in self._parsed_fy_files
        }
        return mixin_import_map
