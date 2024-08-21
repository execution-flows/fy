# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pydantic import BaseModel

from domain.python_entity_name import PythonEntityName


class BaseTemplateModel(BaseModel):
    user_imports: str | None


class FlowTemplateModel(BaseTemplateModel):
    flow_name: PythonEntityName
    return_type: str
