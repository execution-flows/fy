import abc

from jinja2 import Environment, FileSystemLoader

from domain.parsed_fy_file import ParsedFyFileKind
from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC


class GeneratePyFiles_MethodMixin(
    With_ParsedFyFiles_PropertyMixin_ABC,
    abc.ABC
):
    def _generate_py_files(self) -> None:
        for parsed_fy_file in self._parsed_fy_files:
            match parsed_fy_file.file_type:
                case ParsedFyFileKind.FLOW:
                    env = Environment(loader=FileSystemLoader("templates"))
                    template = env.get_template("flow.jinja2")
                    content = template.render(parsed_fy_file.template_model.model_dump())
                    with open(parsed_fy_file.output_py_file_path, "w", encoding="UTF-8") as output_py_file:
                        output_py_file.write(content)
