# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from unittest import TestCase

from constants import FY_PY_FILE_EXTENSION
from flows.fy_py_main_fy import FyPy_Main_Flow


class MainFyPyTestCase(TestCase):

    def _test_main_flow(self, target_folder: str) -> None:
        folder_to_parse = (
            Path(__file__).parent.parent / "test_fy_py_files" / target_folder
        )

        FyPy_Main_Flow(
            folder_to_parse=folder_to_parse,
            project_root_folder=Path(__file__).parent.parent.parent,
        )()

        self.__test_fy_py_files_in_directory(folder_to_parse)

    def __assert_files_equal(
        self, file_to_expect: Path, file_to_generate: Path, comparing_file_path: Path
    ) -> None:
        with (
            file_to_expect.open() as expected_py_file,
            file_to_generate.open() as generated_py_file,
        ):
            self.assertEqual(
                expected_py_file.read(),
                generated_py_file.read(),
                f"Comparing {comparing_file_path}",
            )

    def __test_fy_py_files_in_directory(self, folder_to_parse: Path) -> None:
        fy_files_in_directory = list(folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            self.__assert_files_equal(
                file_to_expect=fy_file_path.with_name(f"{fy_file_path.name}.expected"),
                file_to_generate=fy_file_path,
                comparing_file_path=fy_file_path,
            )
