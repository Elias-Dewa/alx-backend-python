#!/usr/bin/env python3
"""Unit tests for client"""


import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Define a class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, input, mock_get):
        """method that test GithubOrgClient.org and
        returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        self.assertEqual(test_class.org, mock_get.return_value)
        mock_get.assert_called_once_with("https://api.github.com/orgs/"+input)

    def test_public_repos_url(self):
        """Implement the test_public_repos_url method to unit-test"""
        with patch('MyClass.last_transaction',
                   new_callable=PropertyMock) as mock_get:
            mock_get.return_value = payload()
            my_class = GithubOrgClient()
            answer = my_class.__public_repos_url
            mock_get.assert_called_once_with()
