# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
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
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.domain.python_entity_name import PythonEntityName


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
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        raise NotImplementedError()


class ParsedFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.FLOW] = ParsedFyPyFileKind.FLOW
    flow_name: PythonEntityName
    generics_def: str
    declared_base_flow: str
    declared_base_flow_generics_def: str
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return self.file_type, self.flow_name.snake_case


class ParsedBaseFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.BASE_FLOW] = ParsedFyPyFileKind.BASE_FLOW
    base_flow_name: PythonEntityName
    generics_def: str
    declared_base_flow: str
    declared_base_flow_generics_def: str
    annotations: List[Annotation]
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]
    abstract_property_mixins: List[AbstractPropertyModel]
    abstract_method_mixins: List[AbstractMethodModel]

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return self.file_type, self.base_flow_name.snake_case


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
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return entity_key(
            fy_py_kind=self.file_type,
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
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return self.file_type, self.abstract_method_name.snake_case


class ParsedAbstractPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_PROPERTY] = (
        ParsedFyPyFileKind.ABSTRACT_PROPERTY
    )
    abstract_property_name: PythonEntityName
    generics_def: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return self.file_type, self.abstract_property_name.snake_case


class ParsedPropertyFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.PROPERTY] = ParsedFyPyFileKind.PROPERTY
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    generics_def: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return entity_key(
            fy_py_kind=self.file_type,
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
    implementation_name: PythonEntityName

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return entity_key(
            fy_py_kind=self.file_type,
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=PROPERTY_SETTER_IMPLEMENTATION_NAME,
        )
