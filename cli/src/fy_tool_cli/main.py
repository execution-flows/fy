# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
from pathlib import Path

from fy_library import fy


def fy_cli() -> int:
    folder_to_parse = "."
    project_root_folder: str | None = None
    if len(sys.argv) > 1:
        folder_to_parse_index = 1
        if sys.argv[1] == "--root":
            folder_to_parse_index = 3
            project_root_folder = sys.argv[2]
        folder_to_parse = sys.argv[folder_to_parse_index]

    fy(
        folder_to_parse=Path(folder_to_parse),
        project_root_folder=(
            Path(project_root_folder) if project_root_folder is not None else Path.cwd()
        ),
    )
    return 0


if __name__ == "__main__":
    sys.exit(fy_cli())
