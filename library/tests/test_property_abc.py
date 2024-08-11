from unittest import TestCase

from entry.main_flow import Main_Flow
from test_utils.main_flow_text_case import MainFlowTestCase


class TestPropertyAbc(MainFlowTestCase):
    def test_property_abc(self):
        self._test_main_flow(target_folder="mixins/property/greeting")