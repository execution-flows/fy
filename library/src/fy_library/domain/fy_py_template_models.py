# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import abc
from enum import Enum
from typing import List

from pydantic import BaseModel, computed_field

from fy_library.constants import PROPERTY_SETTER_IMPLEMENTATION_NAME
from fy_library.domain.python_entity_name import PythonEntityName


def entity_key(
    mixin_name__snake_case: str, mixin_implementation_name__snake_case: str
) -> str:
    return f"{mixin_name__snake_case}.{mixin_implementation_name__snake_case}"


class MixinModelKind(Enum):
    ABSTRACT_PROPERTY = "abstract_property"
    ABSTRACT_METHOD = "abstract_method"
    PROPERTY = "property"
    METHOD = "method"


class BaseMixinModel(BaseModel):
    kind: MixinModelKind


class AbstractPropertyModel(BaseMixinModel):
    property_name: PythonEntityName


class AbstractMethodModel(BaseMixinModel):
    method_name: PythonEntityName


class PropertyMixinModel(AbstractPropertyModel):
    implementation_name: PythonEntityName


class MethodMixinModel(AbstractMethodModel):
    implementation_name: PythonEntityName


class BaseTemplateModel(BaseModel, abc.ABC):
    python_class_name: PythonEntityName

    @property
    @abc.abstractmethod
    def entity_key(self) -> str:
        raise NotImplementedError()


class FlowTemplateModel(BaseTemplateModel):
    flow_name: PythonEntityName
    return_type: str
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.flow_name.snake_case


class MethodTemplateModel(BaseTemplateModel):
    method_name: PythonEntityName
    implementation_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    abstract_method_mixins: List[AbstractMethodModel]
    arguments: str | None
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.method_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class AbstractMethodTemplateModel(BaseTemplateModel):
    abstract_method_name: PythonEntityName
    arguments: str | None
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.abstract_method_name.snake_case


class AbstractPropertyTemplateModel(BaseTemplateModel):
    abstract_property_name: PythonEntityName
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.abstract_property_name.snake_case


class FlowTemplateModelWithPropertySetters(FlowTemplateModel):
    property_setters: List[AbstractPropertyTemplateModel]


class PropertyTemplateModel(BaseTemplateModel):
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=self.implementation_name.snake_case,
        )


class PropertySetterTemplateModel(BaseTemplateModel):
    property_name: PythonEntityName
    property_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return entity_key(
            mixin_name__snake_case=self.property_name.snake_case,
            mixin_implementation_name__snake_case=PROPERTY_SETTER_IMPLEMENTATION_NAME,
        )
