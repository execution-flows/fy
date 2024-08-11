from pydantic import model_validator
from typing import Any

from domain.template_models import FlowTemplateModel, PropertyTemplateModel
from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.FLOW
        return data


class ParsedPropertyFyFile(ParsedFyFile):
    template_model: PropertyTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.ABSTRACT_PROPERTY
        return data
