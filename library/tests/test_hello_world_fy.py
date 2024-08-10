from unittest import TestCase

from entry.main_flow import Main_Flow


class TestHelloWorldFy(TestCase):
    def test_hello_world_generates_file(self) -> None:
        # TODO: delete `hello_world.py` if exists
        Main_Flow(
            folder_to_parse="tests/test_fy_files/hello_world",
        )()

        with open("library/tests/test_fy_files/hello_world/hello_world.py", "r") as generated_py_file:
            expected = ['from base.execution_flow_base import ExecutionFlowBase', '', '',
                        'class HelloWorld_Flow(ExecutionFlowBase[None]):', '    def __call__(self) -> None:',
                        '        print("Hello world!")', '']

            generated_py_file_lines = generated_py_file.read().split("\n")

            self.assertListEqual(expected, generated_py_file_lines)
