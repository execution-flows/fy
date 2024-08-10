import os
from unittest import TestCase

from entry.main_flow import Main_Flow


class TestHelloWorldFy(TestCase):
    def test_hello_world_generates_file(self) -> None:

        folder_to_parse = "tests/test_fy_files/hello_world"
        file_to_generate = "hello_world.py"

        path = os.path.join(folder_to_parse, file_to_generate)

        if os.path.exists(path):
            os.remove(path)

        Main_Flow(
            folder_to_parse=folder_to_parse,
        )()

        with open(path, "r") as generated_py_file:
            expected = ['from base.execution_flow_base import ExecutionFlowBase', '', '',
                        'class HelloWorld_Flow(ExecutionFlowBase[None]):', '    def __call__(self) -> None:',
                        '        print("Hello world!")', '']

            generated_py_file_lines = generated_py_file.read().split("\n")

            self.assertListEqual(expected, generated_py_file_lines)
