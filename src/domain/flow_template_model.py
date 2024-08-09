from pydantic import BaseModel


class FlowTemplateModel(BaseModel):
    flow_name: str
    flow_body: str
