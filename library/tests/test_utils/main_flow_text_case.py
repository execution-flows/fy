from unittest import TestCase
from pathlib import Path

from entry.main_flow import Main_Flow


class MainFlowTestCase(TestCase):

    def _test_main_flow(self, target_folder: str) -> None:
        folder_to_parse = Path("tests/test_fy_files/", target_folder)

        fy_files_in_directory = list(folder_to_parse.glob("**/*.fy"))
        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            file_to_expect = folder_to_parse / f"{fy_file_path.stem}.py.expected"
            file_to_generate = folder_to_parse / f"{fy_file_path.stem}.py"

            if file_to_generate.exists():
                file_to_generate.unlink()
                assert not file_to_generate.exists()

            Main_Flow(
                folder_to_parse=folder_to_parse,
            )()

            with (
                open(file_to_expect, 'r') as expected_py_file,
                open(file_to_generate, 'r') as generated_py_file
            ):
                self.assertEqual(expected_py_file.read(), generated_py_file.read())
