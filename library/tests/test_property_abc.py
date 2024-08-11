from unittest import TestCase

from entry.main_flow import Main_Flow
from test_utils.main_flow_text_case import MainFlowTestCase


class TestPropertyAbc(TestCase):
    def test_property_abc(self):
        test_case = MainFlowTestCase()
        test_case.main_flow_test_case("mixins/property/greeting")