from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, model_validator

from domain.template_models import FlowTemplateModel


class ParsedFyFileKind(Enum):
    FLOW = "flow"
    ABSTRACT_PROPERTY = "abstract_property"


class ParsedFyFile(BaseModel):
    file_type: ParsedFyFileKind
    output_py_file_path: Path
    template_model: BaseModel


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_file_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.FLOW
        return data
