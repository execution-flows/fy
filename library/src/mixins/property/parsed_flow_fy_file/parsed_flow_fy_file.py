from typing import Any

from pydantic import model_validator

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind
from domain.template_models import FlowTemplateModel


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["kind"] = ParsedFyFileKind.FLOW
        return data
