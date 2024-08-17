# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import Enum
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

from domain.template_models import (
    FlowTemplateModel,
    AbstractPropertyTemplateModel,
    PropertyTemplateModel,
    AbstractMethodTemplateModel,
    MethodTemplateModel,
    BaseTemplateModel,
    PropertySetterTemplateModel,
)


class ParsedFyFileKind(Enum):
    FLOW = "flow"
    ABSTRACT_PROPERTY = "abstract_property"
    ABSTRACT_METHOD = "abstract_method"
    PROPERTY = "property"
    METHOD = "method"
    PROPERTY_SETTER = "property_setter"


class ParsedFyFile(BaseModel):
    file_type: ParsedFyFileKind
    input_fy_file_path: Path
    output_py_file_path: Path
    template_model: BaseTemplateModel


class ParsedFlowFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.FLOW] = ParsedFyFileKind.FLOW
    template_model: FlowTemplateModel


class ParsedAbstractPropertyFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.ABSTRACT_PROPERTY] = (
        ParsedFyFileKind.ABSTRACT_PROPERTY
    )
    template_model: AbstractPropertyTemplateModel


class PropertySetterFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.PROPERTY_SETTER] = (
        ParsedFyFileKind.PROPERTY_SETTER
    )
    template_model: PropertySetterTemplateModel


class ParsedPropertyFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.PROPERTY] = ParsedFyFileKind.PROPERTY
    template_model: PropertyTemplateModel


class ParsedAbstractMethodFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.ABSTRACT_METHOD] = (
        ParsedFyFileKind.ABSTRACT_METHOD
    )
    template_model: AbstractMethodTemplateModel


class ParsedMethodFyFile(ParsedFyFile):
    file_type: Literal[ParsedFyFileKind.METHOD] = ParsedFyFileKind.METHOD
    template_model: MethodTemplateModel
