# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from pathlib import Path

property flow_compose_file_name: Path using parsed_fy_py_file:
    property parsed_fy_py_file
fy"""

import abc
from functools import cached_property

from fy_library.constants import FY_PY_FILE_EXTENSION
from fy_library.mixins.property.flow_compose_file.flow_compose_file_name.abc_fy import (
    FlowComposeFileName_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

from pathlib import Path


# fy:start ===>>>
class FlowComposeFileName_UsingParsedFyPyFile_PropertyMixin(
    # Property Mixins
    FlowComposeFileName_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _flow_compose_file_name(self) -> Path:
        # fy:end <<<===
        assert self._parsed_fy_py_file.file_path.name.endswith(FY_PY_FILE_EXTENSION)
        fc_file_name = f"{self._parsed_fy_py_file.file_path.name[: -len(FY_PY_FILE_EXTENSION)]}_fc.py"
        return self._parsed_fy_py_file.file_path.parent / fc_file_name
