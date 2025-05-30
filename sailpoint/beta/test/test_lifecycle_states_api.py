# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.lifecycle_states_api import LifecycleStatesApi


class TestLifecycleStatesApi(unittest.TestCase):
    """LifecycleStatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LifecycleStatesApi()

    def tearDown(self) -> None:
        pass

    def test_get_lifecycle_states(self) -> None:
        """Test case for get_lifecycle_states

        Get lifecycle state
        """
        pass

    def test_update_lifecycle_states(self) -> None:
        """Test case for update_lifecycle_states

        Update lifecycle state
        """
        pass


if __name__ == '__main__':
    unittest.main()
