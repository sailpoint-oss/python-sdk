# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.vendor_connector_mapping_deleted_at import VendorConnectorMappingDeletedAt

class TestVendorConnectorMappingDeletedAt(unittest.TestCase):
    """VendorConnectorMappingDeletedAt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VendorConnectorMappingDeletedAt:
        """Test VendorConnectorMappingDeletedAt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VendorConnectorMappingDeletedAt`
        """
        model = VendorConnectorMappingDeletedAt()
        if include_optional:
            return VendorConnectorMappingDeletedAt(
                time = '0001-01-01T00:00Z',
                valid = False
            )
        else:
            return VendorConnectorMappingDeletedAt(
        )
        """

    def testVendorConnectorMappingDeletedAt(self):
        """Test VendorConnectorMappingDeletedAt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()