# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, model_validator

from domain.template_models import FlowTemplateModel, AbstractPropertyTemplateModel, PropertyTemplateModel, \
    AbstractMethodTemplateModel, MethodTemplateModel


class ParsedFyFileKind(Enum):
    FLOW = "flow"
    ABSTRACT_PROPERTY = "abstract_property"
    ABSTRACT_METHOD = "abstract_method"
    PROPERTY = "property"
    METHOD = "method"


class ParsedFyFile(BaseModel):
    file_type: ParsedFyFileKind
    input_fy_file_path: Path
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


class ParsedAbstractPropertyFyFile(ParsedFyFile):
    template_model: AbstractPropertyTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_file_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.ABSTRACT_PROPERTY
        return data


class ParsedPropertyFyFile(ParsedFyFile):
    template_model: PropertyTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_file_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.PROPERTY
        return data


class ParsedAbstractMethodFyFile(ParsedFyFile):
    template_model: AbstractMethodTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_file_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.ABSTRACT_METHOD
        return data


class ParsedMethodFyFile(ParsedFyFile):
    template_model: MethodTemplateModel

    @model_validator(mode="before")
    @classmethod
    def set_file_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["file_type"] = ParsedFyFileKind.METHOD
        return data
