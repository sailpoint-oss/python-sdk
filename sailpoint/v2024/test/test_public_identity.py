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

from sailpoint.v2024.models.public_identity import PublicIdentity

class TestPublicIdentity(unittest.TestCase):
    """PublicIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicIdentity:
        """Test PublicIdentity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicIdentity`
        """
        model = PublicIdentity()
        if include_optional:
            return PublicIdentity(
                id = '2c9180857182305e0171993735622948',
                name = 'Alison Ferguso',
                alias = 'alison.ferguso',
                email = 'alison.ferguso@acme-solar.com',
                status = 'Active',
                identity_state = 'ACTIVE',
                manager = sailpoint.v2024.models.identity_reference.IdentityReference(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Thomas Edison', ),
                attributes = [
                    sailpoint.v2024.models.identity_attribute_1.IdentityAttribute_1(
                        key = 'country', 
                        name = 'Country', 
                        value = 'US', )
                    ]
            )
        else:
            return PublicIdentity(
        )
        """

    def testPublicIdentity(self):
        """Test PublicIdentity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()