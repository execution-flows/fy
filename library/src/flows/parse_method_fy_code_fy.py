"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseMethodFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
"""

from base.flow_base import FlowBase
from constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
    PYTHON_ARGUMENTS_REGEX_STRING,
)
from domain.fy_py_template_models import (
    MethodTemplateModel,
    AbstractPropertyModel,
    AbstractMethodModel,
)
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedMethodFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)
from pathlib import Path
from typing import Any, List
import re


# fy:start <<<===
class ParseMethodFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        method_string_split_regex = re.compile(
            rf"method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s*"
            rf"(?P<arguments>\(({PYTHON_ARGUMENTS_REGEX_STRING})\))?\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        )
        method_file_split = method_string_split_regex.split(self._fy_code)

        assert (
            len(method_file_split)
        ) == 7, f"Method file split length {len(method_file_split)} is invalid."

        user_imports = method_file_split[0]
        method_name = PythonEntityName.from_snake_case(method_file_split[1])
        arguments = method_file_split[3]
        return_type = method_file_split[4]
        implementation_name = PythonEntityName.from_snake_case(method_file_split[5])

        abstract_properties: List[AbstractPropertyModel] = []
        abstract_methods: List[AbstractMethodModel] = []

        abstract_property_mixin_regex = re.compile(
            rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        )

        abstract_method_mixin_regex = re.compile(
            rf"^\s+with\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
        )

        mixin_lines = method_file_split[6].split("\n")
        for mixin_line in mixin_lines:
            if mixin_line.strip() == "":
                continue

            declared_abstract_property_mixin = abstract_property_mixin_regex.search(
                mixin_line
            )
            if declared_abstract_property_mixin is not None:
                abstract_properties.append(
                    AbstractPropertyModel(
                        property_name=PythonEntityName.from_snake_case(
                            declared_abstract_property_mixin.group(
                                "abstract_property_name"
                            )
                        )
                    )
                )
                continue

            declared_abstract_method_mixin = abstract_method_mixin_regex.search(
                mixin_line
            )
            if declared_abstract_method_mixin is not None:
                abstract_methods.append(
                    AbstractMethodModel(
                        method_name=PythonEntityName.from_snake_case(
                            declared_abstract_method_mixin.group("abstract_method_name")
                        )
                    )
                )
                continue

        parsed_fy_py_file = ParsedMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=user_imports,
            template_model=MethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
                ),
                method_name=method_name,
                implementation_name=implementation_name,
                abstract_property_mixins=abstract_properties,
                abstract_method_mixins=abstract_methods,
                arguments=arguments,
                return_type=return_type,
            ),
        )
        return parsed_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        pre_marker_file_content: str,
        post_marker_file_content: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        self._fy_py_file_to_parse = fy_py_file_to_parse
        self._pre_marker_file_content = pre_marker_file_content
        self._post_marker_file_content = post_marker_file_content
        super().__init__(*args, **kwargs)
