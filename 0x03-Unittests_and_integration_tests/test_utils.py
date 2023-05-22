#!/usr/bin/env python3
"""Unit tests"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """A class that inherit from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Implement method to test that the method returns
        what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, result):
        """Implement method to test that a KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, result)


class TestGetJson(unittest.TestCase):
    """A class that inherit from unittest.TestCase"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Implement method to test that"""
        with patch("requests.get") as request:
            request.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Implement a class"""

    def test_memoize(self):
        """Implement method to test"""
        class TestClass:
            """Define a class"""

            def a_method(self):
                """a method that returns a number 42"""
                return 42

            @memoize
            def a_property(self):
                """a method that returns a memoized property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as result_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            result_method.assert_called_once_with()
