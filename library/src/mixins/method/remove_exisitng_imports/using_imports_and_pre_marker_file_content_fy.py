# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


method remove_existing_imports(mixin_imports: List[str], pre_marker_file_content: str, user_imports: str) -> List[str]
using imports_and_pre_marker_file_content:
"""

from typing import List, Set

from constants import IMPORT_REGEX


# fy:start ===>>>
class RemoveExistingImports_UsingImportsAndPreMarkerFileContent_MethodMixin:
    def _remove_existing_imports(
        self, mixin_imports: List[str], pre_marker_file_content: str, user_imports: str
    ) -> List[str]:
        # fy:end <<<===
        pre_marker_imports: Set[str] = set()
        for pre_marker_line in pre_marker_file_content.split("\n"):
            import_regex_result = IMPORT_REGEX.search(pre_marker_line)
            if import_regex_result is not None:
                pre_marker_imports.add(
                    import_regex_result.group("from")
                    or import_regex_result.group("import")
                )

        mixin_imports_result = []
        for mixin_import in mixin_imports:
            import_regex_result = IMPORT_REGEX.search(mixin_import)
            import_part = import_regex_result.group(
                "from"
            ) or import_regex_result.group("import")
            if import_part not in pre_marker_imports:
                mixin_imports_result.append(mixin_import)

        user_imports_results = []
        for user_import in user_imports.split("\n"):
            if user_import == "":
                continue
            import_regex_result = IMPORT_REGEX.search(user_import)
            import_part = import_regex_result.group(
                "from"
            ) or import_regex_result.group("import")
            if import_part not in pre_marker_imports:
                user_imports_results.append(user_import)

        return mixin_imports_result + user_imports_results
