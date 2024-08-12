import sys
from pathlib import Path

import fy_library


def main() -> int:
    folder_to_parse = "."
    if len(sys.argv) > 1:
        folder_to_parse = sys.argv[1]

    fy_library.Main_Flow(
        folder_to_parse=Path(folder_to_parse)
    )()
    return 0


if __name__ == "__main__":
    sys.exit(main())
