# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from enum import Enum


class ParsedFyPyFileKind(str, Enum):
    FLOW = "flow"
    BASE_FLOW = "base_flow"
    METHOD = "method"
    ABSTRACT_METHOD = "abstract_method"
    ABSTRACT_PROPERTY = "abstract_property"
    PROPERTY = "property"
    PROPERTY_SETTER = "property_setter"
