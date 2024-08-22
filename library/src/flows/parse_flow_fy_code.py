from base.execution_flow_base import ExecutionFlowBase

from mixins.property.fy_code.using_setter import FyCode_UsingSetter_PropertyMixin

import re
from typing import Any

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from domain.fy_py_template_models import FlowTemplateModel
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFlowFyPyFile
from domain.python_entity_name import PythonEntityName


class ParseFlowFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
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
        # flow_string_body = flow_file_split[-1]

        parsed_fy_py_file = ParsedFlowFyPyFile(
            template_model=FlowTemplateModel(
                user_imports=user_imports,
                flow_name=flow_name,
                return_type=return_type,
            )
        )

        return parsed_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        super().__init__(*args, **kwargs)