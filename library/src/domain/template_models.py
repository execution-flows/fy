# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import List

from pydantic import BaseModel

from domain.python_entity_name import PythonEntityName


class BaseTemplateModel(BaseModel):
    python_class_name: PythonEntityName


class AbstractPropertyTemplateModel(BaseTemplateModel):
    abstract_property_name: PythonEntityName
    return_type: str


class PropertyTemplateModel(BaseTemplateModel):
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    return_type: str
    property_body: str


class PropertyMixinModel(BaseModel):
    property_name: PythonEntityName
    implementation_name: PythonEntityName


class MethodMixinModel(BaseModel):
    method_name: PythonEntityName
    implementation_name: PythonEntityName


class AbstractPropertyModel(BaseModel):
    property_name: PythonEntityName


class FlowTemplateModel(BaseTemplateModel):
    flow_name: PythonEntityName
    properties: List[PropertyMixinModel]
    methods: List[MethodMixinModel]
    return_type: str
    flow_call_body: str


class AbstractMethodTemplateModel(BaseTemplateModel):
    abstract_method_name: PythonEntityName
    arguments: str
    return_type: str


class MethodTemplateModel(BaseTemplateModel):
    method_name: PythonEntityName
    implementation_name: PythonEntityName
    abstract_property_mixins: List[AbstractPropertyModel]
    arguments: str | None
    return_type: str
    method_body: str
