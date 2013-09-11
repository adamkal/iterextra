# -*- coding: utf-8 -*-

import unittest
import mock

import iterextra


class IterExtraTestCase(unittest.TestCase):

    def test_chaincall(self):
        chaincall = iterextra.chaincall

        func1 = mock.MagicMock()
        func2 = mock.MagicMock()

        #  single function
        result = chaincall(func1)("arg1", "arg2", kwarg1="kwarg1",
                                  kwarg2="kwarg2")
        func1.assert_called_once_with("arg1", "arg2", kwarg1="kwarg1",
                                      kwarg2="kwarg2")
        self.assertEquals(result, func1.return_value)
        func1.reset_mock()

        # two simple values
        result = chaincall(func1, func2)("arg1", "arg2", kwarg1="kwarg1",
                                         kwarg2="kwarg2")
        func1.assert_called_once_with("arg1", "arg2", kwarg1="kwarg1",
                                      kwarg2="kwarg2")
        func2.assert_called_once_with(func1.return_value)
        self.assertEquals(result, func2.return_value)
        func1.reset_mock()
        func2.reset_mock()
