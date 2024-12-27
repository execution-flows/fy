# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from enum import Enum
from pathlib import Path
from typing import Literal, List
import abc
from pydantic import BaseModel, computed_field

from fy_library.constants import PROPERTY_SETTER_IMPLEMENTATION_NAME
from fy_library.domain.annotation_object import Annotation
from fy_library.domain.entity_key import entity_key
from fy_library.domain.mixin_models import (
    MethodMixinModel,
    AbstractMethodModel,
    AbstractPropertyModel,
    PropertyMixinModel,
    MixinModelKind,
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
    python_class_name: PythonEntityName

    @property
    @abc.abstractmethod
    def entity_key(self) -> str:
        raise NotImplementedError()


class ParsedFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.FLOW] = ParsedFyPyFileKind.FLOW
    flow_name: PythonEntityName
    generics_def: str
    declared_base_flow: str
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.flow_name.snake_case


class ParsedBaseFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.BASE_FLOW] = ParsedFyPyFileKind.BASE_FLOW
    base_flow_name: PythonEntityName
    generics_def: str
    declared_base_flow: str
    annotations: List[Annotation]
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]
    abstract_property_mixins: List[AbstractPropertyModel]
    abstract_method_mixins: List[AbstractMethodModel]

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.base_flow_name.snake_case


class ParsedMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.METHOD] = ParsedFyPyFileKind.METHOD
    method_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    abstract_method_mixins: List[AbstractMethodModel]
    generics_def: str
    arguments: str | None
    implementation_name: PythonEntityName
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.method_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class ParsedAbstractMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_METHOD] = (
        ParsedFyPyFileKind.ABSTRACT_METHOD
    )
    abstract_method_name: PythonEntityName
    generics_def: str
    arguments: str | None
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.abstract_method_name.snake_case


def convert_parsed_abstract_method_fy_py_file_to_abstract_method_mixin(
    parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile,
) -> AbstractMethodModel:
    return AbstractMethodModel(
        python_class_name=parsed_abstract_method_fy_py_file.python_class_name,
        kind=MixinModelKind.ABSTRACT_METHOD,
        method_name=parsed_abstract_method_fy_py_file.abstract_method_name,
        generics_impl=parsed_abstract_method_fy_py_file.generics_def,
    )


class ParsedAbstractPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_PROPERTY] = (
        ParsedFyPyFileKind.ABSTRACT_PROPERTY
    )
    abstract_property_name: PythonEntityName
    generics_def: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.abstract_property_name.snake_case


class ParsedPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.PROPERTY] = ParsedFyPyFileKind.PROPERTY
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    generics_def: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class PropertySetterFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.PROPERTY_SETTER] = (
        ParsedFyPyFileKind.PROPERTY_SETTER
    )
    property_name: PythonEntityName
    generics_def: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=PROPERTY_SETTER_IMPLEMENTATION_NAME,
        )
