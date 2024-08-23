# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from enum import Enum

from domain.fy_py_template_models import (
    FlowTemplateModel,
    BaseTemplateModel,
    MethodTemplateModel,
    AbstractMethodTemplateModel,
)


class ParsedFyPyFileKind(Enum):
    FLOW = "flow"
    METHOD = "method"
    ABSTRACT_METHOD = "abstract_method"


class FyPyFileParts(BaseModel):
    fy_code: str
    pre_marker_file_content: str
    post_marker_file_content: str


class ParsedFyPyFile(FyPyFileParts):
    file_type: ParsedFyPyFileKind
    file_path: Path
    template_model: BaseTemplateModel


class ParsedFlowFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.FLOW] = ParsedFyPyFileKind.FLOW
    template_model: FlowTemplateModel


class ParsedMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.METHOD] = ParsedFyPyFileKind.METHOD
    template_model: MethodTemplateModel


class ParsedAbstractMethodFyPyFile(ParsedFyPyFile):
    file_type: Literal[ParsedFyPyFileKind.ABSTRACT_METHOD] = (
        ParsedFyPyFileKind.ABSTRACT_METHOD
    )
    template_model: AbstractMethodTemplateModel
