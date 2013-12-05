# -*- coding: utf-8 -*-

import unittest
import mock

import iterextra


class _TestObj(object):

    def __init__(self, arg):
        self.attribute = arg

    @property
    def property(self):
        return self.attribute + " parameter"

    def method(self):
        return self.attribute + " method"


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

        self.assertTrue(chaincall.__doc__,
                        "'chaincall' function lacks documentation")

    def test_pick(self):
        pick = iterextra.pick

        obj = _TestObj("test")

        self.assertEquals(pick("attribute")(obj), "test")
        self.assertEquals(pick("property")(obj), "test parameter")
        self.assertEquals(pick("method")(obj)(), "test method")
        self.assertRaises(AttributeError, pick('non_existent_member'), obj)

        self.assertTrue(pick.__doc__,
                        "'pick' function lacks documentation")
        self.assertEquals(pick("my_member").__doc__,
                          "Picks member 'my_member' from ``obj``")
        self.assertEquals(pick("my_member").__name__, "my_member_picker")
