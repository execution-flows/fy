import pathlib
from typing import cast, List

from jinja2 import Environment, FileSystemLoader

from domain.template_models import entity_key

from domain.parsed_fy_file import (
    ParsedFyFileKind,
    ParsedFlowFyFile,
    ParsedPropertyFyFile,
    ParsedMethodFyFile,
    ParsedFyFile,
)


method generate_py_files using jinja2_templates:
    with property parsed_fy_files
    with property required_property_setters
    with property mixin_import_map

    def -> None:
        self.__generate_py_files__using_parsed_fy_files()
        self.__generate_py_files__using_required_property_setters()

    def __generate_py_files__using_parsed_fy_files(self) -> None:
        for parsed_fy_file in self._parsed_fy_files:
            match parsed_fy_file.file_type:
                case ParsedFyFileKind.FLOW:
                    mixin_imports = [
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=property_mixin.property_name.snake_case,
                                mixin_implementation_name__snake_case=property_mixin.implementation_name.snake_case,
                            )
                        ]
                        for property_mixin in cast(
                            ParsedFlowFyFile, parsed_fy_file
                        ).template_model.properties
                    ] + [
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=method_mixin.method_name.snake_case,
                                mixin_implementation_name__snake_case=method_mixin.implementation_name.snake_case,
                            )
                        ]
                        for method_mixin in cast(
                            ParsedFlowFyFile, parsed_fy_file
                        ).template_model.methods
                    ]
                    load_jinja2_template(
                        jinja2_template_name="flow.jinja2",
                        mixin_imports=mixin_imports,
                        parsed_fy_file=parsed_fy_file,
                    )
                case ParsedFyFileKind.ABSTRACT_PROPERTY:
                    load_jinja2_template(
                        jinja2_template_name="abstract_property.jinja2",
                        mixin_imports=[],
                        parsed_fy_file=parsed_fy_file,
                    )
                case ParsedFyFileKind.PROPERTY:
                    mixin_imports = [
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedPropertyFyFile, parsed_fy_file
                        ).template_model.abstract_property_mixins
                    ]
                    load_jinja2_template(
                        jinja2_template_name="property.jinja2",
                        mixin_imports=mixin_imports,
                        parsed_fy_file=parsed_fy_file,
                    )
                case ParsedFyFileKind.ABSTRACT_METHOD:
                    load_jinja2_template(
                        jinja2_template_name="abstract_method.jinja2",
                        mixin_imports=[],
                        parsed_fy_file=parsed_fy_file,
                    )
                case ParsedFyFileKind.METHOD:
                    mixin_imports = [
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedMethodFyFile, parsed_fy_file
                        ).template_model.abstract_property_mixins
                    ] + [
                        self._mixin_import_map[
                            abstract_method_mixin.method_name.snake_case
                        ]
                        for abstract_method_mixin in cast(
                            ParsedMethodFyFile, parsed_fy_file
                        ).template_model.abstract_method_mixins
                    ]
                    load_jinja2_template(
                        jinja2_template_name="method.jinja2",
                        mixin_imports=mixin_imports,
                        parsed_fy_file=parsed_fy_file,
                    )

    def __generate_py_files__using_required_property_setters(self) -> None:
        for parsed_fy_file in self._required_property_setters:
            load_jinja2_template(
                jinja2_template_name="property_setter.jinja2",
                mixin_imports=[],
                parsed_fy_file=parsed_fy_file,
            )


def load_jinja2_template(
    jinja2_template_name: str, mixin_imports: List[str], parsed_fy_file: ParsedFyFile
) -> None:
    templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template_name)
    template_model = parsed_fy_file.template_model.model_dump()
    template_model["mixin_imports"] = mixin_imports
    content = template.render(template_model)
    with open(
        file=parsed_fy_file.output_py_file_path, mode="w", encoding="UTF-8"
    ) as output_py_file:
        output_py_file.write(content)