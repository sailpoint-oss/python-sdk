# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.field_details_dto import FieldDetailsDto

class TestFieldDetailsDto(unittest.TestCase):
    """FieldDetailsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldDetailsDto:
        """Test FieldDetailsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldDetailsDto`
        """
        model = FieldDetailsDto()
        if include_optional:
            return FieldDetailsDto(
                name = 'userName',
                transform = {type=rule, attributes={name=Create Unique LDAP Attribute}},
                attributes = {template=${firstname}.${lastname}${uniqueCounter}, cloudMaxUniqueChecks=50, cloudMaxSize=20, cloudRequired=true},
                is_required = False,
                type = 'string',
                is_multi_valued = False
            )
        else:
            return FieldDetailsDto(
        )
        """

    def testFieldDetailsDto(self):
        """Test FieldDetailsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
