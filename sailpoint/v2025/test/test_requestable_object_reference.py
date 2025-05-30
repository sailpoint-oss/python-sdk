# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.requestable_object_reference import RequestableObjectReference

class TestRequestableObjectReference(unittest.TestCase):
    """RequestableObjectReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestableObjectReference:
        """Test RequestableObjectReference
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestableObjectReference`
        """
        model = RequestableObjectReference()
        if include_optional:
            return RequestableObjectReference(
                id = '2c9180835d2e5168015d32f890ca1581',
                name = 'Applied Research Access',
                description = 'Access to research information, lab results, and schematics',
                type = 'ROLE'
            )
        else:
            return RequestableObjectReference(
        )
        """

    def testRequestableObjectReference(self):
        """Test RequestableObjectReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
