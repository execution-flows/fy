from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class ParsedFyFileKind(Enum):
    FLOW = "flow"


class ParsedFyFile(BaseModel):
    file_type: ParsedFyFileKind
    output_py_file_path: Path
    template_model: BaseModel
