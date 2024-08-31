# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import re
from pathlib import Path
from unittest import TestCase

from constants import FY_PY_FILE_EXTENSION, FY_START_MARKER, FY_END_MARKER
from flows.fy_py_main_fy import FyPy_Main_Flow


class MainFyPyTestCase(TestCase):

    def _test_main_flow(
        self, target_folder: str, perform_fy_code_deletion: bool = True
    ) -> None:
        folder_to_parse = (
            Path(__file__).parent.parent / "test_fy_py_files" / target_folder
        )

        if perform_fy_code_deletion:
            self.__remove_fy_generated_code_from_generated_files(folder_to_parse)

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

    def __remove_fy_generated_code_from_generated_files(
        self, folder_to_parse: Path
    ) -> None:
        fy_files_in_directory = list(folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            with open(file=fy_file_path, mode="r") as f:
                file_content = f.read()

            generated_content_regex = re.compile(
                r"^(?P<pre_generated_code>.*)"
                rf"{FY_START_MARKER}.*{FY_END_MARKER}\n"
                r"(?P<post_generated_code>.*)$",
                flags=re.DOTALL,
            )
            generated_content_search = generated_content_regex.search(file_content)

            with open(file=fy_file_path, mode="w") as f:
                f.write(
                    f"{generated_content_search.group('pre_generated_code')}"
                    f"{FY_START_MARKER}\n"
                    f"{FY_END_MARKER}\n"
                    f"{generated_content_search.group('post_generated_code')}"
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
