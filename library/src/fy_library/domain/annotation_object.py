# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from enum import Enum

from pydantic import BaseModel


class AnnotationKind(str, Enum):
    CALLABLE = "@callable"


class Annotation(BaseModel):
    kind: AnnotationKind
