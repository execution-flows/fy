# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
import pathlib
from typing import cast, List

from jinja2 import Environment, FileSystemLoader

from domain.parsed_fy_file import ParsedFyFileKind, ParsedFyFile, ParsedFlowFyFile
from mixins.property.mixin_import_map.abc import With_MixinImportMap_PropertyMixin_ABC
from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC


def load_jinja2_template(jinja2_template_name: str, mixin_imports: List[str], parsed_fy_file: ParsedFyFile) -> None:
    templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template_name)
    template_model = parsed_fy_file.template_model.model_dump()
    template_model["mixin_imports"] = mixin_imports
    content = template.render(template_model)
    with open(parsed_fy_file.output_py_file_path, "w", encoding="UTF-8") as output_py_file:
        output_py_file.write(content)


class GeneratePyFiles_UsingJinja2Templates_MethodMixin(
    With_ParsedFyFiles_PropertyMixin_ABC,
    With_MixinImportMap_PropertyMixin_ABC,
    abc.ABC
):

    def _generate_py_files(self) -> None:
        for parsed_fy_file in self._parsed_fy_files:
            match parsed_fy_file.file_type:
                case ParsedFyFileKind.FLOW:
                    mixin_imports = [
                        self._mixin_import_map[
                            mixin.property_name.snake_case + "." + mixin.implementation_name.snake_case
                            ]
                        for mixin in cast(ParsedFlowFyFile, parsed_fy_file).template_model.properties
                    ] + [
                        self._mixin_import_map[
                            mixin.method_name.snake_case + "." + mixin.implementation_name.snake_case
                        ]
                        for mixin in cast(ParsedFlowFyFile, parsed_fy_file).template_model.methods
                    ]
                    load_jinja2_template("flow.jinja2", mixin_imports, parsed_fy_file)
                case ParsedFyFileKind.ABSTRACT_PROPERTY:
                    load_jinja2_template("abstract_property.jinja2", [], parsed_fy_file)
                case ParsedFyFileKind.PROPERTY:
                    load_jinja2_template("property.jinja2", [], parsed_fy_file)
                case ParsedFyFileKind.ABSTRACT_METHOD:
                    load_jinja2_template("abstract_method.jinja2", [], parsed_fy_file)
                case ParsedFyFileKind.METHOD:
                    load_jinja2_template("method.jinja2", [], parsed_fy_file)
