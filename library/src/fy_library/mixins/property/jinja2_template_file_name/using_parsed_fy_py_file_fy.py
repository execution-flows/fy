# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property jinja2_template_file_name: str using parsed_fy_py_file:
    property parsed_fy_py_file
"""

import abc
from functools import cached_property

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

from fy_library.mixins.property.jinja2_template_file_name.abc_fy import (
    Jinja2TemplateFileName_PropertyMixin_ABC,
)


# fy:start ===>>>
class Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    Jinja2TemplateFileName_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _jinja2_template_file_name(self) -> str:
        # fy:end <<<===
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                return "flow.jinja2"
            case ParsedFyPyFileKind.BASE_FLOW:
                return "base_flow.jinja2"
            case ParsedFyPyFileKind.METHOD:
                return "method.jinja2"
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                return "abstract_method.jinja2"
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                return "abstract_property.jinja2"
            case ParsedFyPyFileKind.PROPERTY:
                return "property.jinja2"
            case _:
                raise NotImplementedError(
                    f"No Execution Flow kind for {self._parsed_fy_py_file.file_type}"
                )
