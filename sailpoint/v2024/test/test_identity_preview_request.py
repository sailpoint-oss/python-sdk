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

from sailpoint.v2024.models.identity_preview_request import IdentityPreviewRequest

class TestIdentityPreviewRequest(unittest.TestCase):
    """IdentityPreviewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityPreviewRequest:
        """Test IdentityPreviewRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityPreviewRequest`
        """
        model = IdentityPreviewRequest()
        if include_optional:
            return IdentityPreviewRequest(
                identity_id = '',
                identity_attribute_config = [
                    sailpoint.v2024.models.identity_attribute_config.IdentityAttributeConfig(
                        enabled = True, 
                        attribute_transforms = [
                            sailpoint.v2024.models.identity_attribute_transform.IdentityAttributeTransform(
                                identity_attribute_name = 'email', 
                                transform_definition = sailpoint.v2024.models.transform_definition.TransformDefinition(
                                    type = 'accountAttribute', 
                                    attributes = {attributeName=e-mail, sourceName=MySource, sourceId=2c9180877a826e68017a8c0b03da1a53}, ), )
                            ], )
                    ]
            )
        else:
            return IdentityPreviewRequest(
        )
        """

    def testIdentityPreviewRequest(self):
        """Test IdentityPreviewRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()