# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property flow_compose_file_content: str using parsed_fy_py_file:
    property parsed_fy_py_file
    property generated_flow_compose_code
fy"""

import abc
from functools import cached_property
from typing import cast

from fy_library.domain.parsed_fy_py_file import (
    ParsedPropertyFyPyFile,
    ParsedMethodFyPyFile,
    ParsedFlowFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.flow_compose_file.flow_compose_file_content.abc_fy import (
    FlowComposeFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

from fy_library.mixins.property.templates.generated_flow_compose_code.abc_fy import (
    GeneratedFlowComposeCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class FlowComposeFileContent_UsingParsedFyPyFile_PropertyMixin(
    # Property Mixins
    FlowComposeFileContent_PropertyMixin_ABC,
    GeneratedFlowComposeCode_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _flow_compose_file_content(self) -> str:
        # fy:end <<<===
        replaced_file_content = self._parsed_fy_py_file.post_marker_file_content
        method_mixin_names: list[str] = []
        property_mixin_names: list[str] = []
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.PROPERTY:
                property_mixin_names = list(
                    map(
                        lambda p: p.property_name.snake_case,
                        cast(
                            ParsedPropertyFyPyFile, self._parsed_fy_py_file
                        ).abstract_property_mixins,
                    )
                )
            case ParsedFyPyFileKind.METHOD:
                property_mixin_names = list(
                    map(
                        lambda p: p.property_name.snake_case,
                        cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).abstract_property_mixins,
                    )
                )
                method_mixin_names = list(
                    map(
                        lambda p: p.method_name.snake_case,
                        cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).abstract_method_mixins,
                    )
                )
            case ParsedFyPyFileKind.FLOW:
                property_mixin_names = list(
                    map(
                        lambda p: p.property_name.snake_case,
                        cast(ParsedFlowFyPyFile, self._parsed_fy_py_file).properties,
                    )
                )
                method_mixin_names = list(
                    map(
                        lambda p: p.method_name.snake_case,
                        cast(ParsedFlowFyPyFile, self._parsed_fy_py_file).methods,
                    )
                )

        for mixin_name in property_mixin_names:
            self_mixin = f"self._{mixin_name}"
            function_call = f"{mixin_name}()"
            replaced_file_content = replaced_file_content.replace(
                self_mixin, function_call
            )

        for mixin_name in method_mixin_names:
            self_mixin = f"self._{mixin_name}"
            function_call = mixin_name
            replaced_file_content = replaced_file_content.replace(
                self_mixin, function_call
            )

        stripped_tab_lines = map(
            lambda line: line[4:],
            replaced_file_content.splitlines(),
        )
        stripped_tab_content = "\n".join(stripped_tab_lines)
        return f"{self._generated_flow_compose_code}\n{stripped_tab_content}\n"
