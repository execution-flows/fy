from test_utils.main_flow_text_case import MainFlowTestCase


class TestHelloIntegerFy(MainFlowTestCase):
    def test_hello_integer_generates_file(self) -> None:
        self._test_main_flow(target_folder="hello_integer")
