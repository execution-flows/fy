# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import abc
from enum import Enum

from pydantic import BaseModel, computed_field

from fy_library.domain.entity_key import entity_key
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
    def entity_key(self) -> str:
        raise NotImplementedError()


class AbstractMethodModel(BaseMixinModel):
    method_name: PythonEntityName
    generics_impl: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.method_name.snake_case


class MethodMixinModel(AbstractMethodModel):
    implementation_name: PythonEntityName

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.method_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class AbstractPropertyModel(BaseMixinModel):
    property_name: PythonEntityName
    generics_impl: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.property_name.snake_case


class PropertyMixinModel(AbstractPropertyModel):
    implementation_name: PythonEntityName

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )
