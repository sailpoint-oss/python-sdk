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

from sailpoint.v2024.models.service_desk_integration_dto1_all_of_cluster_ref import ServiceDeskIntegrationDto1AllOfClusterRef

class TestServiceDeskIntegrationDto1AllOfClusterRef(unittest.TestCase):
    """ServiceDeskIntegrationDto1AllOfClusterRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDeskIntegrationDto1AllOfClusterRef:
        """Test ServiceDeskIntegrationDto1AllOfClusterRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDeskIntegrationDto1AllOfClusterRef`
        """
        model = ServiceDeskIntegrationDto1AllOfClusterRef()
        if include_optional:
            return ServiceDeskIntegrationDto1AllOfClusterRef(
                type = 'CLUSTER',
                id = '2c9180847a7fccdd017aa5896f9f4f6f',
                name = 'Training VA'
            )
        else:
            return ServiceDeskIntegrationDto1AllOfClusterRef(
        )
        """

    def testServiceDeskIntegrationDto1AllOfClusterRef(self):
        """Test ServiceDeskIntegrationDto1AllOfClusterRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()