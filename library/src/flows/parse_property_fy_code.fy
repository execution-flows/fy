import re
from pathlib import Path
from typing import Any

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from domain.fy_py_template_models import PropertyTemplateModel
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedPropertyFyPyFile
from domain.python_entity_name import PythonEntityName


flow ParsePropertyFyCode:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter

    def -> ParsedFyPyFile:
        property_regex = re.compile(
            rf"property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})"
            rf"\s*:\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        )

        property_file_split = property_regex.split(self._fy_code)

        assert len(
            property_file_split
        ) == 5, f"Property file split length {len(property_file_split)} is invalid"

        property_name = PythonEntityName.from_snake_case(property_file_split[1])
        property_type = property_file_split[2]
        implementation_name =  PythonEntityName.from_snake_case(property_file_split[3])

        parsed_fy_py_file = ParsedPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            template_model=PropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
                ),
                property_name=property_name,
                implementation_name=implementation_name,
                property_type=property_type,
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
