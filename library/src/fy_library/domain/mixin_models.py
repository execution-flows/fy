# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import abc
from enum import Enum

from pydantic import BaseModel, computed_field

from fy_library.constants import (
    GENERATED_PROPERTY_FILE_IMPLEMENTATION_NAMES,
    PROPERTY_SETTER_IMPLEMENTATION_NAME,
)
from fy_library.domain.entity_key import entity_key
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.domain.python_entity_name import PythonEntityName


class MixinModelKind(Enum):
    ABSTRACT_PROPERTY = "abstract_property"
    ABSTRACT_METHOD = "abstract_method"
    PROPERTY = "property"
    METHOD = "method"


class BaseMixinModel(BaseModel, abc.ABC):
    python_class_name: PythonEntityName
    kind: MixinModelKind

    @property
    @abc.abstractmethod
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        raise NotImplementedError()


class AbstractMethodModel(BaseMixinModel):
    method_name: PythonEntityName
    generics_impl: str
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return ParsedFyPyFileKind(self.kind.value), self.method_name.snake_case


class MethodMixinModel(AbstractMethodModel):
    implementation_name: PythonEntityName

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return entity_key(
            fy_py_kind=ParsedFyPyFileKind(self.kind.value),
            mixin_name__snake_case=self.method_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class AbstractPropertyModel(BaseMixinModel):
    property_name: PythonEntityName
    generics_impl: str
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        return ParsedFyPyFileKind(self.kind.value), self.property_name.snake_case


class PropertyMixinModel(AbstractPropertyModel):
    implementation_name: PythonEntityName
    constant_value: str

    @computed_field
    @property
    def entity_key(self) -> tuple[ParsedFyPyFileKind, str]:
        fy_py_kind = (
            ParsedFyPyFileKind.PROPERTY_SETTER
            if self.implementation_name.snake_case
            in GENERATED_PROPERTY_FILE_IMPLEMENTATION_NAMES
            else ParsedFyPyFileKind.PROPERTY
        )
        return entity_key(
            fy_py_kind=fy_py_kind,
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case
            if fy_py_kind != ParsedFyPyFileKind.PROPERTY_SETTER
            else PROPERTY_SETTER_IMPLEMENTATION_NAME,
        )
