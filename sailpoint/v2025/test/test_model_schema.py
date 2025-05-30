# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.model_schema import ModelSchema

class TestModelSchema(unittest.TestCase):
    """ModelSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelSchema:
        """Test ModelSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelSchema`
        """
        model = ModelSchema()
        if include_optional:
            return ModelSchema(
                id = '2c9180835d191a86015d28455b4a2329',
                name = 'account',
                native_object_type = 'User',
                identity_attribute = 'sAMAccountName',
                display_attribute = 'distinguishedName',
                hierarchy_attribute = 'memberOf',
                include_permissions = False,
                features = [PROVISIONING, NO_PERMISSIONS_PROVISIONING, GROUPS_HAVE_MEMBERS],
                configuration = {groupMemberAttribute=member},
                attributes = [{name=sAMAccountName, type=STRING, isMultiValued=false, isEntitlement=false, isGroup=false}, {name=memberOf, type=STRING, schema={type=CONNECTOR_SCHEMA, id=2c9180887671ff8c01767b4671fc7d60, name=group}, description=Group membership, isMultiValued=true, isEntitlement=true, isGroup=true}],
                created = '2019-12-24T22:32:58.104Z',
                modified = '2019-12-31T20:22:28.104Z'
            )
        else:
            return ModelSchema(
        )
        """

    def testModelSchema(self):
        """Test ModelSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
