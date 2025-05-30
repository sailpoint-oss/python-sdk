# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.identity_access import IdentityAccess

class TestIdentityAccess(unittest.TestCase):
    """IdentityAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityAccess:
        """Test IdentityAccess
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityAccess`
        """
        model = IdentityAccess()
        if include_optional:
            return IdentityAccess(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'John Doe',
                display_name = 'John Q. Doe',
                description = '',
                type = 'ROLE',
                source = sailpoint.v2024.models.reference.Reference(
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'John Doe', ),
                owner = None,
                revocable = True,
                privileged = False,
                attribute = 'memberOf',
                value = 'CN=Buyer,OU=Groups,OU=Demo,DC=seri,DC=sailpointdemo,DC=com',
                standalone = False,
                disabled = True
            )
        else:
            return IdentityAccess(
        )
        """

    def testIdentityAccess(self):
        """Test IdentityAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
