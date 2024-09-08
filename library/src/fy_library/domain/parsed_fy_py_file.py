# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pathlib import Path
from typing import Literal, List

from pydantic import BaseModel, computed_field
from enum import Enum

from fy_library.domain.fy_py_template_models import (
    BaseTemplateModel,
    MethodTemplateModel,
    AbstractMethodTemplateModel,
    AbstractPropertyTemplateModel,
    PropertyTemplateModel,
    PropertySetterTemplateModel,
    BaseFlowTemplateModel,
    PropertyMixinModel,
    MethodMixinModel,
)
from fy_library.domain.python_entity_name import PythonEntityName


class ParsedFyPyFileKind(Enum):
    FLOW = "flow"
    BASE_FLOW = "base_flow"
    METHOD = "method"
    ABSTRACT_METHOD = "abstract_method"
    ABSTRACT_PROPERTY = "abstract_property"
    PROPERTY = "property"
    PROPERTY_SETTER = "property_setter"


class FyPyFileParts(BaseModel):
    pre_fy_code: str
    fy_code: str
    pre_marker_file_content: str
    post_marker_file_content: str


class ParsedFyPyFile(FyPyFileParts):
    file_type: ParsedFyPyFileKind
    file_path: Path
    user_imports: str
    template_model: BaseTemplateModel


class ParsedFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.FLOW] = ParsedFyPyFileKind.FLOW
    flow_name: PythonEntityName
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.flow_name.snake_case


class ParsedBaseFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.BASE_FLOW] = ParsedFyPyFileKind.BASE_FLOW
    template_model: BaseFlowTemplateModel


class ParsedMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.METHOD] = ParsedFyPyFileKind.METHOD
    template_model: MethodTemplateModel


class ParsedAbstractMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_METHOD] = (
        ParsedFyPyFileKind.ABSTRACT_METHOD
    )
    template_model: AbstractMethodTemplateModel


class ParsedAbstractPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_PROPERTY] = (
        ParsedFyPyFileKind.ABSTRACT_PROPERTY
    )
    template_model: AbstractPropertyTemplateModel


class ParsedPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.PROPERTY] = ParsedFyPyFileKind.PROPERTY
    template_model: PropertyTemplateModel


class PropertySetterFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.PROPERTY_SETTER] = (
        ParsedFyPyFileKind.PROPERTY_SETTER
    )
    template_model: PropertySetterTemplateModel
