# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import abc

from pydantic import BaseModel, computed_field

from domain.python_entity_name import PythonEntityName


def entity_key(
    mixin_name__snake_case: str, mixin_implementation_name__snake_case: str
) -> str:
    return f"{mixin_name__snake_case}.{mixin_implementation_name__snake_case}"


class BaseTemplateModel(BaseModel, abc.ABC):
    python_class_name: PythonEntityName

    @property
    @abc.abstractmethod
    def entity_key(self) -> str:
        raise NotImplementedError()


class FlowTemplateModel(BaseTemplateModel):
    flow_name: PythonEntityName
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.flow_name.snake_case


class MethodTemplateModel(BaseTemplateModel):
    method_name: PythonEntityName
    implementation_name: PythonEntityName
    arguments: str | None
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.method_name.snake_case


class AbstractMethodTemplateModel(BaseTemplateModel):
    abstract_method_name: PythonEntityName
    arguments: str
    return_type: str

    @computed_field
    @property
    def entity_key(self) -> str:
        return self.abstract_method_name.snake_case
