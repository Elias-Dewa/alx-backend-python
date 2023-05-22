#!/usr/bin/env python3
"""Unit tests for client"""


import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Define a class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    def test_org(self, input, mock_get):
        """method that test GithubOrgClient.org and
        returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock_get.assert_called_once_with("https://api.github.com/orgs/"+input)
