# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
from pathlib import Path

from fy_library import Main_Flow


def main() -> int:
    folder_to_parse = "."
    if len(sys.argv) > 1:
        folder_to_parse = sys.argv[1]

    Main_Flow(folder_to_parse=Path(folder_to_parse))()
    return 0


if __name__ == "__main__":
    sys.exit(main())
