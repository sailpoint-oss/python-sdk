# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v2024.models.outlier_feature_summary_outlier_feature_display_values_inner import OutlierFeatureSummaryOutlierFeatureDisplayValuesInner

class TestOutlierFeatureSummaryOutlierFeatureDisplayValuesInner(unittest.TestCase):
    """OutlierFeatureSummaryOutlierFeatureDisplayValuesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutlierFeatureSummaryOutlierFeatureDisplayValuesInner:
        """Test OutlierFeatureSummaryOutlierFeatureDisplayValuesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OutlierFeatureSummaryOutlierFeatureDisplayValuesInner`
        """
        model = OutlierFeatureSummaryOutlierFeatureDisplayValuesInner()
        if include_optional:
            return OutlierFeatureSummaryOutlierFeatureDisplayValuesInner(
                display_name = 'Aliza Chris',
                value = '55',
                value_type = 'INTEGER'
            )
        else:
            return OutlierFeatureSummaryOutlierFeatureDisplayValuesInner(
        )
        """

    def testOutlierFeatureSummaryOutlierFeatureDisplayValuesInner(self):
        """Test OutlierFeatureSummaryOutlierFeatureDisplayValuesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()