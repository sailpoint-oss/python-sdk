# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.approval_comment1 import ApprovalComment1

class TestApprovalComment1(unittest.TestCase):
    """ApprovalComment1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApprovalComment1:
        """Test ApprovalComment1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApprovalComment1`
        """
        model = ApprovalComment1()
        if include_optional:
            return ApprovalComment1(
                author = sailpoint.v2025.models.approval_identity.ApprovalIdentity(
                    id = '85d173e7d57e496569df763231d6deb6a', 
                    type = 'IDENTITY', 
                    name = 'John Doe', ),
                comment = 'Looks good',
                created_date = '2023-04-12T23:20:50.52Z'
            )
        else:
            return ApprovalComment1(
        )
        """

    def testApprovalComment1(self):
        """Test ApprovalComment1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
