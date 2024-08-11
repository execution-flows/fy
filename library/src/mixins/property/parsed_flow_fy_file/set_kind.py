from pydantic import model_validator
from typing import Any

from domain.template_models import FlowTemplateModel
from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["kind"] = ParsedFyFileKind.FLOW
            data["kind"] = ParsedFyFileKind.PROPERTY
        return data
