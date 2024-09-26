# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from enum import Enum

from pydantic import BaseModel
from fy_library.domain.python_entity_name import PythonEntityName


class MixinModelKind(Enum):
    ABSTRACT_PROPERTY = "abstract_property"
    ABSTRACT_METHOD = "abstract_method"
    PROPERTY = "property"
    METHOD = "method"


class BaseMixinModel(BaseModel):
    python_class_name: PythonEntityName
    kind: MixinModelKind


class AbstractMethodModel(BaseMixinModel):
    method_name: PythonEntityName


class MethodMixinModel(AbstractMethodModel):
    implementation_name: PythonEntityName


class AbstractPropertyModel(BaseMixinModel):
    property_name: PythonEntityName


class PropertyMixinModel(AbstractPropertyModel):
    implementation_name: PythonEntityName
