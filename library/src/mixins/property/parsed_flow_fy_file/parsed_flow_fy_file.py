from pydantic import model_validator
from typing import Any

from domain.flow_template_model import FlowTemplateModel
from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["kind"] = ParsedFyFileKind.FLOW
        return data
