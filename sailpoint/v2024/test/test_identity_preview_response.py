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

from sailpoint.v2024.models.identity_preview_response import IdentityPreviewResponse

class TestIdentityPreviewResponse(unittest.TestCase):
    """IdentityPreviewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityPreviewResponse:
        """Test IdentityPreviewResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityPreviewResponse`
        """
        model = IdentityPreviewResponse()
        if include_optional:
            return IdentityPreviewResponse(
                identity = sailpoint.v2024.models.identity_preview_response_identity.IdentityPreviewResponse_identity(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                preview_attributes = [
                    sailpoint.v2024.models.identity_attribute_preview.IdentityAttributePreview(
                        name = 'email', 
                        value = email@mail.com, 
                        previous_value = oldEmail@mail.com, 
                        error_messages = [
                            sailpoint.v2024.models.error_message_dto.ErrorMessageDto(
                                locale = 'en-US', 
                                locale_origin = 'DEFAULT', 
                                text = 'The request was syntactically correct but its content is semantically invalid.', )
                            ], )
                    ]
            )
        else:
            return IdentityPreviewResponse(
        )
        """

    def testIdentityPreviewResponse(self):
        """Test IdentityPreviewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()