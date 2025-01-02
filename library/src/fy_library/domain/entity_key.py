# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


def entity_key(
    fy_py_kind: ParsedFyPyFileKind,
    mixin_name__snake_case: str,
    mixin_implementation_name__snake_case: str,
) -> tuple[ParsedFyPyFileKind, str]:
    return (
        fy_py_kind,
        f"{mixin_name__snake_case}.{mixin_implementation_name__snake_case}",
    )
