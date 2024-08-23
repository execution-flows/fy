import re
from pathlib import Path
from typing import Any
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedAbstractMethodFyPyFile
from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING, PYTHON_ARGUMENTS_REGEX_STRING
from domain.python_entity_name import PythonEntityName
from domain.fy_py_template_models import AbstractMethodTemplateModel


flow ParseAbstractMethodFyCode:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter

    def -> ParsedFyPyFile:
        abstract_method_regex = re.compile(
            rf"method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*(\((?P<arguments>{PYTHON_ARGUMENTS_REGEX_STRING})\))?"
            rf"\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        )

        abstract_method_file_split = abstract_method_regex.split(self._fy_code)

        print(abstract_method_file_split)

        assert len(
            abstract_method_file_split
        ) == 6, f"Abstract Method file split length {len(abstract_method_file_split)} is invalid"

        abstract_method_name = PythonEntityName.from_snake_case(abstract_method_file_split[1])
        arguments = abstract_method_name[3]
        return_type = abstract_method_name[4]

        parsed_fy_py_file = ParsedAbstractMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            template_model=AbstractMethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{abstract_method_name.pascal_case}_MethodMixin_ABC"
                ),
                flow_name=abstract_method_name,
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
