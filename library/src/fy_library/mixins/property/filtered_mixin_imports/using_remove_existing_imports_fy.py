# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property filtered_mixin_imports: List[str] using remove_existing_imports:
    property mixin_imports
    property parsed_fy_py_file
"""

import abc
import re
from functools import cached_property
from typing import List, Final

from fy_library.mixins.property.filtered_mixin_imports.abc_fy import (
    FilteredMixinImports_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_imports.abc_fy import (
    MixinImports_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

_IMPORT_REGEX: Final = re.compile(
    r"^(?P<from>from [\w.]+) import (?P<from_classes>.*)\s*$|^(?P<import>import [\w.]+)$",
    flags=re.DOTALL,
)


# fy:start ===>>>
class FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin(
    # Property_mixins
    FilteredMixinImports_PropertyMixin_ABC,
    MixinImports_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _filtered_mixin_imports(self) -> List[str]:
        # fy:end <<<===
        pre_marker_imports = set(
            self.__collect_import_classes(
                import_lines=self._parsed_fy_py_file.pre_marker_file_content.split(
                    "\n"
                ),
                pre_marker_imports=set(),
            )
        )

        mixin_imports_result = self.__collect_import_classes(
            import_lines=self._mixin_imports, pre_marker_imports=pre_marker_imports
        )

        user_imports_results = self.__collect_import_classes(
            import_lines=self._parsed_fy_py_file.user_imports.split("\n"),
            pre_marker_imports=pre_marker_imports,
        )

        def import_sort_key(import_line: str) -> str:
            import_line_split = import_line.split(" ")
            return "".join(
                ["0" if import_line_split[0] == "import" else "1"]
                + import_line_split[1:]
            )

        return self.__format_imports(
            sorted(list(mixin_imports_result), key=lambda i: import_sort_key(i))
            + sorted(list(user_imports_results), key=lambda i: import_sort_key(i))
        )

    def __format_imports(self, imports: list[str]) -> list[str]:
        result_imports: list[str] = []
        for import_line in imports:
            if import_line.startswith("import ") or len(import_line) <= 88:
                result_imports.append(import_line)
                continue
            import_line_parts = import_line.split(" ")
            result_imports.append(
                f"{' '.join(import_line_parts[:-1])} (\n{' ' * 4}{import_line_parts[-1]},\n)"
            )

        return result_imports

    def __collect_import_classes(
        self,
        import_lines: list[str],
        pre_marker_imports: set[str],
    ) -> list[str]:
        result_imports: list[str] = []

        def import_line_generate_and_append(import_classes: str, from_package: str):
            for import_class in import_classes.split(","):
                import_class = import_class.strip()
                if import_class != "":
                    generated_import_line = f"{from_package} import {import_class}"
                    if generated_import_line not in pre_marker_imports:
                        result_imports.append(generated_import_line)

        collecting_from_import: str | None = None

        for pre_marker_line in import_lines:
            if collecting_from_import is not None:
                end_of_imports = pre_marker_line.strip().endswith(")")
                if end_of_imports:
                    pre_marker_line = pre_marker_line.strip()[:-1]
                import_line_generate_and_append(
                    import_classes=pre_marker_line, from_package=collecting_from_import
                )
                if end_of_imports:
                    collecting_from_import = None

                continue

            import_regex_result = _IMPORT_REGEX.search(pre_marker_line)
            if import_regex_result is None:
                continue

            import_line = import_regex_result.group("import")
            if import_line is not None:
                if import_line not in pre_marker_imports:
                    result_imports.append(import_line)
                continue

            from_import = import_regex_result.group("from")
            assert from_import is not None
            from_classes = import_regex_result.group("from_classes")
            assert from_classes is not None

            start_of_collection = from_classes.strip().startswith("(")
            if start_of_collection:
                from_classes = from_classes.strip()[1:]
            import_line_generate_and_append(
                import_classes=from_classes, from_package=from_import
            )
            if start_of_collection:
                collecting_from_import = from_import
            continue

        return result_imports
