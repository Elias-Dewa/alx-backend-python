# 0x03. Unittests and Integration Tests

![image](<https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T072928Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20a578c84e43a5f802b99a85c5016120cb3675aa6a2b0f35ccb6fe8892079178>
)
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

    $ python -m unittest path/to/test_file.py

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Required Files

### utils.py (or download)

    # !/usr/bin/env python3
    """Generic utilities for github org client.
    """
    import requests
    from functools import wraps
    from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable,
    )

    __all__ = [
        "access_nested_map",
        "get_json",
        "memoize",
    ]

    def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
        """Access nested map with key path.
        Parameters
        ----------
        nested_map: Mapping
            A nested map
        path: Sequence
            a sequence of key representing a path to the value
        Example
        -------
        >>> nested_map = {"a": {"b": {"c": 1}}}
        >>> access_nested_map(nested_map, ["a", "b", "c"])
        1
        """
        for key in path:
            if not isinstance(nested_map, Mapping):
                raise KeyError(key)
            nested_map = nested_map[key]

        return nested_map

    def get_json(url: str) -> Dict:
        """Get JSON from remote URL.
        """
        response = requests.get(url)
        return response.json()

    def memoize(fn: Callable) -> Callable:
        """Decorator to memoize a method.
        Example
        -------
        class MyClass:
            @memoize
            def a_method(self):
                print("a_method called")
                return 42
        >>> my_object = MyClass()
        >>> my_object.a_method
        a_method called
        42
        >>> my_object.a_method
        42
        """
        attr_name = "_{}".format(fn.__name__)

        @wraps(fn)
        def memoized(self):
            """"memoized wraps"""
            if not hasattr(self, attr_name):
                setattr(self, attr_name, fn(self))
            return getattr(self, attr_name)

        return property(memoized)

### client.py (or download)
    # !/usr/bin/env python3
    """A github org client
    """
    from typing import (
        List,
        Dict,
    )

    from utils import (
        get_json,
        access_nested_map,
        memoize,
    )

    class GithubOrgClient:
        """A Githib org client
        """
        ORG_URL = "<https://api.github.com/orgs/{org}>"

        def __init__(self, org_name: str) -> None:
            """Init method of GithubOrgClient"""
            self._org_name = org_name

        @memoize
        def org(self) -> Dict:
            """Memoize org"""
            return get_json(self.ORG_URL.format(org=self._org_name))

        @property
        def _public_repos_url(self) -> str:
            """Public repos URL"""
            return self.org["repos_url"]

        @memoize
        def repos_payload(self) -> Dict:
            """Memoize repos payload"""
            return get_json(self._public_repos_url)

        def public_repos(self, license: str = None) -> List[str]:
            """Public repos"""
            json_payload = self.repos_payload
            public_repos = [
                repo["name"] for repo in json_payload
                if license is None or self.has_license(repo, license)
            ]

            return public_repos

        @staticmethod
        def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
            """Static: has_license"""
            assert license_key is not None, "license_key cannot be None"
            try:
                has_license = access_nested_map(repo, ("license", "key")) == license_key
            except KeyError:
                return False
            return has_license

### fixtures.py (or download)


## Solutions for mandatory and advanced tasks...