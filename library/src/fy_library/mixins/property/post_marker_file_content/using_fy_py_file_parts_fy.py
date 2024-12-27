# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property post_marker_file_content: str using fy_py_file_parts:
    property fy_py_file_parts
"""

import abc
from functools import cached_property

from fy_library.mixins.property.fy_py_file_parts.abc_fy import (
    FyPyFileParts_PropertyMixin_ABC,
)

from fy_library.mixins.property.post_marker_file_content.abc_fy import (
    PostMarkerFileContent_PropertyMixin_ABC,
)


# fy:start ===>>>
class PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    FyPyFileParts_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _post_marker_file_content(self) -> str:
        # fy:end <<<===
        post_marker_file_content = self._fy_py_file_parts.post_marker_file_content
        return post_marker_file_content
