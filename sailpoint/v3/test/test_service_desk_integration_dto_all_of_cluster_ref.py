# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.service_desk_integration_dto_all_of_cluster_ref import ServiceDeskIntegrationDtoAllOfClusterRef

class TestServiceDeskIntegrationDtoAllOfClusterRef(unittest.TestCase):
    """ServiceDeskIntegrationDtoAllOfClusterRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDeskIntegrationDtoAllOfClusterRef:
        """Test ServiceDeskIntegrationDtoAllOfClusterRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDeskIntegrationDtoAllOfClusterRef`
        """
        model = ServiceDeskIntegrationDtoAllOfClusterRef()
        if include_optional:
            return ServiceDeskIntegrationDtoAllOfClusterRef(
                type = 'CLUSTER',
                id = '2c9180847a7fccdd017aa5896f9f4f6f',
                name = 'Training VA'
            )
        else:
            return ServiceDeskIntegrationDtoAllOfClusterRef(
        )
        """

    def testServiceDeskIntegrationDtoAllOfClusterRef(self):
        """Test ServiceDeskIntegrationDtoAllOfClusterRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()