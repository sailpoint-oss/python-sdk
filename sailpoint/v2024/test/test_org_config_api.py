# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.api.org_config_api import OrgConfigApi


class TestOrgConfigApi(unittest.TestCase):
    """OrgConfigApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrgConfigApi()

    def tearDown(self) -> None:
        pass

    def test_get_org_config(self) -> None:
        """Test case for get_org_config

        Get org config settings
        """
        pass

    def test_get_valid_time_zones(self) -> None:
        """Test case for get_valid_time_zones

        Get valid time zones
        """
        pass

    def test_patch_org_config(self) -> None:
        """Test case for patch_org_config

        Patch org config
        """
        pass


if __name__ == '__main__':
    unittest.main()
