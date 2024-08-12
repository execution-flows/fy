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


class FlowTemplateModel(BaseTemplateModel):
    flow_name: PythonEntityName
    properties: List[PropertyMixinModel]
    return_type: str
    flow_call_body: str
