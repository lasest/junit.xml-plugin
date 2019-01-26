import os
from unittest.mock import MagicMock, patch

from . import PluginTestCase


class Given_TCMS_RUN_ID_IsPresent(PluginTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.plugin._rpc = MagicMock()
        cls.plugin._rpc.TestRun.create = MagicMock()
        cls.plugin._rpc.TestRun.get_cases = MagicMock(return_value=[])

    def test_when_get_run_id_then_will_use_it(self):
        with patch.dict(os.environ, {
                'TCMS_RUN_ID': '532',
        }):
            run_id = self.plugin.get_run_id()
            self.assertEqual(run_id, 532)
            self.plugin._rpc.TestRun.create.assert_not_called()


class Given_TCMS_RUN_ID_IsNotPresent(PluginTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.plugin._rpc = MagicMock()
        cls.plugin.get_product_id = MagicMock(return_value=(44, 'p.Test'))
        cls.plugin.get_version_id = MagicMock(return_value=(55, 'v.Test'))
        cls.plugin.get_build_id = MagicMock(return_value=(66, 'b.Test'))
        cls.plugin.get_plan_id = MagicMock(return_value=77)

        cls.plugin._rpc.User.filter = MagicMock(return_value=[{'id': 88}])

        cls.plugin._rpc.TestRun.create = MagicMock(return_value={'run_id': 99})
        cls.plugin._rpc.TestRun.get_cases = MagicMock(return_value=[])

    def test_when_get_run_id_then_will_create_TestRun(self):
        with patch.dict(os.environ, {}):
            run_id = self.plugin.get_run_id()
            self.assertEqual(run_id, 99)
            self.plugin._rpc.TestRun.create.assert_called_with({
                'summary': '[TAP] Results for p.Test, v.Test, b.Test',
                'manager': 88,
                'plan': 77,
                'build': 66,
            })


class TestCaseRunMixin:
    def test_when_parsing_results_are_updated(self):
        self.fail('not implemented')


class GivenEmptyTestRun(PluginTestCase, TestCaseRunMixin):
    def test_when_parsing_then_TestCase_is_added(self):
        self.fail('not implemented')


class GivenTestRunWithTestCases(PluginTestCase, TestCaseRunMixin):
    def test_when_parsing_then_existing_TestCase_is_not_added(self):
        self.fail('not implemented')
