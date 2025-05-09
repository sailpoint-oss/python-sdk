# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.api.iai_outliers_api import IAIOutliersApi


class TestIAIOutliersApi(unittest.TestCase):
    """IAIOutliersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IAIOutliersApi()

    def tearDown(self) -> None:
        pass

    def test_export_outliers_zip(self) -> None:
        """Test case for export_outliers_zip

        IAI Identity Outliers Export
        """
        pass

    def test_get_identity_outlier_snapshots(self) -> None:
        """Test case for get_identity_outlier_snapshots

        IAI Identity Outliers Summary
        """
        pass

    def test_get_identity_outliers(self) -> None:
        """Test case for get_identity_outliers

        IAI Get Identity Outliers
        """
        pass

    def test_get_latest_identity_outlier_snapshots(self) -> None:
        """Test case for get_latest_identity_outlier_snapshots

        IAI Identity Outliers Latest Summary
        """
        pass

    def test_get_outlier_contributing_feature_summary(self) -> None:
        """Test case for get_outlier_contributing_feature_summary

        Get identity outlier contibuting feature summary
        """
        pass

    def test_get_peer_group_outliers_contributing_features(self) -> None:
        """Test case for get_peer_group_outliers_contributing_features

        Get identity outlier's contibuting features
        """
        pass

    def test_ignore_identity_outliers(self) -> None:
        """Test case for ignore_identity_outliers

        IAI Identity Outliers Ignore
        """
        pass

    def test_list_outliers_contributing_feature_access_items(self) -> None:
        """Test case for list_outliers_contributing_feature_access_items

        Gets a list of access items associated with each identity outlier contributing feature
        """
        pass

    def test_un_ignore_identity_outliers(self) -> None:
        """Test case for un_ignore_identity_outliers

        IAI Identity Outliers Unignore
        """
        pass


if __name__ == '__main__':
    unittest.main()
