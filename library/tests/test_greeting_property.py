from test_utils.main_flow_text_case import MainFlowTestCase


class TestGreetingProperty(MainFlowTestCase):
    def test_greeting_property(self):
        self._test_main_flow(target_folder="mixins/property/greeting")
