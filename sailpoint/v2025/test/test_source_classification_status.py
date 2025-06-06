# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.source_classification_status import SourceClassificationStatus

class TestSourceClassificationStatus(unittest.TestCase):
    """SourceClassificationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceClassificationStatus:
        """Test SourceClassificationStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceClassificationStatus`
        """
        model = SourceClassificationStatus()
        if include_optional:
            return SourceClassificationStatus(
                status = 'COMPLETED',
                started = '2017-07-11T18:45:37.098Z',
                updated = '2018-06-25T20:22:28.104Z',
                counts = sailpoint.v2025.models.source_classification_status_all_of_counts.SourceClassificationStatus_allOf_counts(
                    expected = 1000, 
                    received = 800, 
                    completed = 500, )
            )
        else:
            return SourceClassificationStatus(
        )
        """

    def testSourceClassificationStatus(self):
        """Test SourceClassificationStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
