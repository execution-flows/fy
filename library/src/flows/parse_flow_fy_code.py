from base.execution_flow_base import ExecutionFlowBase

from mixins.property.fy_code.using_setter import FyCode_UsingSetter_PropertyMixin
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)

import re
from typing import Any
from pathlib import Path

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from domain.fy_py_template_models import FlowTemplateModel
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFlowFyPyFile
from domain.python_entity_name import PythonEntityName


class ParseFlowFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    # Base
    ExecutionFlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        flow_string_split_regex = re.compile(
            rf"flow\s+(?P<flow_name>{FY_ENTITY_REGEX_STRING})\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING}):\s*\n"
        )

        flow_file_split = flow_string_split_regex.split(self._fy_code)

        assert (
            len(flow_file_split)
        ) == 4, f"Flow file length {len(flow_file_split)} is invalid."

        user_imports = flow_file_split[0]
        flow_name = PythonEntityName.from_snake_case(flow_file_split[1])
        return_type = flow_file_split[2]

        parsed_fy_py_file = ParsedFlowFyPyFile(
            file_path=self._fy_py_file_to_parse,
            template_model=FlowTemplateModel(
                user_imports=user_imports,
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{flow_name}_Flow"
                ),
                flow_name=flow_name,
                return_type=return_type,
            ),
        )

        return parsed_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)
