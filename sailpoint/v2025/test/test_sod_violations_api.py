# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.api.sod_violations_api import SODViolationsApi


class TestSODViolationsApi(unittest.TestCase):
    """SODViolationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SODViolationsApi()

    def tearDown(self) -> None:
        pass

    def test_start_predict_sod_violations(self) -> None:
        """Test case for start_predict_sod_violations

        Predict sod violations for identity.
        """
        pass

    def test_start_violation_check(self) -> None:
        """Test case for start_violation_check

        Check sod violations
        """
        pass


if __name__ == '__main__':
    unittest.main()
