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
from typing import List, Set, Final

from fy_library.mixins.property.mixin_imports.abc_fy import (
    MixinImports_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

_IMPORT_REGEX: Final = re.compile(
    r"^(?P<from>from [\w.]+) import .*$|^(?P<import>import [\w.]+)$", flags=re.DOTALL
)


# fy:start ===>>>
class FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin(
    # Property_mixins
    MixinImports_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _filtered_mixin_imports(self) -> List[str]:
        # fy:end <<<===
        pre_marker_imports: Set[str] = set()
        for pre_marker_line in self._parsed_fy_py_file.pre_marker_file_content.split(
            "\n"
        ):
            import_regex_result = _IMPORT_REGEX.search(pre_marker_line)
            if import_regex_result is not None:
                pre_marker_imports.add(
                    import_regex_result.group("from")
                    or import_regex_result.group("import")
                )

        mixin_imports_result = []
        for mixin_import in self._mixin_imports:
            import_regex_result = _IMPORT_REGEX.search(mixin_import)
            import_part = import_regex_result.group(
                "from"
            ) or import_regex_result.group("import")
            if import_part not in pre_marker_imports:
                mixin_imports_result.append(mixin_import)

        user_imports_results = []
        for user_import in self._parsed_fy_py_file.user_imports.split("\n"):
            if user_import == "":
                continue
            import_regex_result = _IMPORT_REGEX.search(user_import)
            import_part = import_regex_result.group(
                "from"
            ) or import_regex_result.group("import")
            if import_part not in pre_marker_imports:
                user_imports_results.append(user_import)

        return mixin_imports_result + user_imports_results
