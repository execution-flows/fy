from pathlib import Path
from typing import List


property fy_py_files_to_parse using files_discovery:
    with property folder_to_parse

    @cached
    def -> List[Path]:
        return []
