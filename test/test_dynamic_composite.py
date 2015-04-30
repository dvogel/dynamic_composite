# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest

from dynamic_composite import DynamicComposite

__all__ = ['TestDynamicCompositeOrdering']


class Vi(object):
    operating_systems = ['unix']
    terminals = ['VT100', 'VT220']


class Vim(object):
    operating_systems = ['unix', 'windows', 'macos']


class GVim(object):
    operating_systems = ['unix', 'windows']
    gui = 'gtk'


class MVim(object):
    operating_systems = ['macos']
    gui = 'xquartz'


class TestDynamicCompositeOrdering(unittest.TestCase):

    def setUp(self):
        self.vi = Vi()
        self.vim = Vim()
        self.gvim = GVim()
        self.mvim = MVim()
        self.comp = DynamicComposite(
            self.vi, self.vim, self.gvim, self.mvim
        )

    def test_operating_systems(self):
        self.assertEqual(self.comp.operating_systems,
                         self.vi.operating_systems)

    def test_gui(self):
        self.assertEqual(self.comp.gui,
                         self.gvim.gui)

    def test_missing_attr(self):
        with self.assertRaises(AttributeError):
            self.an_attribute_not_on_any_subordinate_object

if __name__ == '__main__':
    unittest.main()

