# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from unittest import TestCase


class MainFyPyTestCase(TestCase):

    def _test_main_flow(self, target_folder: str) -> None:
        folder_to_parse = (
            Path(__file__).parent.parent / "test_fypy_files" / target_folder
        )

        # TODO: change to FyPy_Main_Flow once we have it
        # FyPy_Main_Flow(
        #     folder_to_parse=folder_to_parse,
        #     project_root_folder=Path(__file__).parent.parent,
        # )()

        self.__test_fy_files_in_directory(folder_to_parse)

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

    def __test_fy_files_in_directory(self, folder_to_parse: Path) -> None:
        fy_files_in_directory = list(folder_to_parse.rglob("*.fy.py"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            self.__assert_files_equal(
                file_to_expect=fy_file_path.parent / f"{fy_file_path.stem}.py.expected",
                file_to_generate=fy_file_path.parent / f"{fy_file_path.stem}.py",
                comparing_file_path=fy_file_path,
            )
