from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, model_validator

from domain.flow_template_model import FlowTemplateModel


class ParsedFyFileKind(Enum):
    FLOW = "flow"


class ParsedFyFile(BaseModel):
    file_type: ParsedFyFileKind
    output_py_file_path: Path
    template_model: BaseModel


class ParsedFlowFyFile(ParsedFyFile):
    template_model: FlowTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_kind(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["kind"] = ParsedFyFileKind.FLOW
        return data
