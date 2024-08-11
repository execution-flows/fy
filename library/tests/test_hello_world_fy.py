from unittest import TestCase

from test_utils.main_flow_text_case import MainFlowTestCase


class TestHelloWorldFy(TestCase):
    def test_hello_world_generates_file(self) -> None:
        test_case = MainFlowTestCase()
        test_case.main_flow_test_case("hello_world")
