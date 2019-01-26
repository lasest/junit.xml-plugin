import unittest
from unittest.mock import patch
from tap_plugin import main


class MainFuncTestCase(unittest.TestCase):
    def test_when_calling_main_with_arguments_then_parse(self):
        with patch('tap_plugin.Plugin.parse') as parse:
            main([__file__, 'output.tap'])
            parse.assert_called_with('output.tap')

    def test_when_calling_main_without_arguments_then_usage(self):
        with self.assertRaisesRegex(Exception,
                                    'USAGE: %s results.tap' % __file__):
            main([__file__])
