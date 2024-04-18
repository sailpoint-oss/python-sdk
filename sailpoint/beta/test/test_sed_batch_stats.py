# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.sed_batch_stats import SedBatchStats

class TestSedBatchStats(unittest.TestCase):
    """SedBatchStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SedBatchStats:
        """Test SedBatchStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SedBatchStats`
        """
        model = SedBatchStats()
        if include_optional:
            return SedBatchStats(
                batch_complete = True,
                batch_id = '016629d1-1d25-463f-97f3-0c6686846650',
                discovered_count = 100,
                discovery_complete = True,
                processed_count = 100
            )
        else:
            return SedBatchStats(
        )
        """

    def testSedBatchStats(self):
        """Test SedBatchStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()