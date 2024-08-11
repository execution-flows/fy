from pydantic import BaseModel


class FlowTemplateModel(BaseModel):
    flow_name: str
    return_type: str
    flow_call_body: str


class PropertyTemplateModel(BaseModel):
    property_name: str
    return_type: str
