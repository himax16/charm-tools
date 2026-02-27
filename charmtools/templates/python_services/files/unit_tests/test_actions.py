#!/usr/bin/env python

import sys
import mock
import unittest

try:
    import importlib.resources

    def resource_filename(package, resource):
        """Return the filename for the given resource"""
        return str(importlib.resources.files(package).joinpath(resource))
except ImportError:
    from pkg_resources import resource_filename

# allow importing actions from the hooks directory
sys.path.append(resource_filename(__name__, '../hooks'))
import actions


class TestActions(unittest.TestCase):
    @mock.patch('charmhelpers.core.hookenv.log')
    def test_log_start(self, log):
        actions.log_start('test-service')
        log.assert_called_once_with('$metadata.package starting')


if __name__ == '__main__':
    unittest.main()
