import os
from unittest import TestCase

from entry.main_flow import Main_Flow
from test_utils.main_flow_text_case import MainFlowTestCase


class TestHelloIntegerFy(TestCase):
    def test_hello_integer_generates_file(self) -> None:
        test_case = MainFlowTestCase()
        test_case.main_flow_test_case("hello_integer")
