# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.attribute_definition_schema import AttributeDefinitionSchema

class TestAttributeDefinitionSchema(unittest.TestCase):
    """AttributeDefinitionSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeDefinitionSchema:
        """Test AttributeDefinitionSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeDefinitionSchema`
        """
        model = AttributeDefinitionSchema()
        if include_optional:
            return AttributeDefinitionSchema(
                type = 'CONNECTOR_SCHEMA',
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'group'
            )
        else:
            return AttributeDefinitionSchema(
        )
        """

    def testAttributeDefinitionSchema(self):
        """Test AttributeDefinitionSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
