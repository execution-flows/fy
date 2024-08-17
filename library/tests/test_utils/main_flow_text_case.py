# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from unittest import TestCase
from pathlib import Path

from entry.main_flow import Main_Flow


class MainFlowTestCase(TestCase):

    def _test_main_flow(self, target_folder: str) -> None:
        folder_to_parse = Path(__file__).parent.parent / "test_fy_files" / target_folder

        fy_files_in_directory = list(folder_to_parse.rglob("*.fy"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            file_to_expect = fy_file_path.parent / f"{fy_file_path.stem}.py.expected"
            file_to_generate = fy_file_path.parent / f"{fy_file_path.stem}.py"

            if file_to_generate.exists():
                file_to_generate.unlink()
                assert not file_to_generate.exists()

            Main_Flow(
                folder_to_parse=folder_to_parse,
                project_root_folder=Path(__file__).parent.parent,
            )()

            with (
                file_to_expect.open() as expected_py_file,
                file_to_generate.open() as generated_py_file,
            ):
                self.assertEqual(
                    expected_py_file.read(),
                    generated_py_file.read(),
                    f"Comparing {fy_file_path}",
                )
