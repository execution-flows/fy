# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from unittest import TestCase
from pathlib import Path

from entry.main_flow import Main_Flow


class MainFlowTestCase(TestCase):

    def _test_main_flow(self, target_folder: str) -> None:
        folder_to_parse = Path(__file__).parent.parent / "test_fy_files" / target_folder
        self.__delete_py_files(folder_to_parse)

        Main_Flow(
            folder_to_parse=folder_to_parse,
            project_root_folder=Path(__file__).parent.parent.parent,
        )()

        self.__test_fy_files_in_directory(folder_to_parse)
        self.__test_property_using_setter_py_files(folder_to_parse)

    def __delete_py_files(self, folder_to_parse: Path) -> None:
        py_files_in_directory = list(folder_to_parse.rglob("*.py"))
        for py_file_path in py_files_in_directory:
            if not py_file_path.is_file():
                continue

            if py_file_path.exists():
                py_file_path.unlink()
                assert not py_file_path.exists()

    def __test_property_using_setter_py_files(self, folder_to_parse: Path) -> None:
        py_files_in_directory = list(folder_to_parse.rglob("using_setter.py"))
        fy_files_in_directory = set(folder_to_parse.rglob("using_setter.fy"))

        for py_file_path in py_files_in_directory:
            if not py_file_path.is_file():
                continue

            if (
                py_file_path.with_name(f"{py_file_path.stem}.fy")
                in fy_files_in_directory
            ):
                continue

            self.__assert_files_equal(
                file_to_expect=py_file_path.parent / f"{py_file_path.stem}.py.expected",
                file_to_generate=py_file_path.parent / f"{py_file_path.stem}.py",
                comparing_file_path=py_file_path,
            )

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
        fy_files_in_directory = list(folder_to_parse.rglob("*.fy"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            self.__assert_files_equal(
                file_to_expect=fy_file_path.parent / f"{fy_file_path.stem}.py.expected",
                file_to_generate=fy_file_path.parent / f"{fy_file_path.stem}.py",
                comparing_file_path=fy_file_path,
            )
