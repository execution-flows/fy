from pydantic import BaseModel

from domain.python_entity_name import PythonEntityName


class FlowTemplateModel(BaseModel):
    flow_name: PythonEntityName
    return_type: str
    flow_call_body: str


class AbstractPropertyTemplateModel(BaseModel):
    abstract_property_name: PythonEntityName
    return_type: str


class PropertyTemplateModel(BaseModel):
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    return_type: str
    property_body: str
