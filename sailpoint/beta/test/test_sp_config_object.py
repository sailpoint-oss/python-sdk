# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.models.sp_config_object import SpConfigObject

class TestSpConfigObject(unittest.TestCase):
    """SpConfigObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpConfigObject:
        """Test SpConfigObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpConfigObject`
        """
        model = SpConfigObject()
        if include_optional:
            return SpConfigObject(
                object_type = 'TRIGGER_SUBSCRIPTION',
                reference_extractors = [$.owner],
                signature_required = False,
                always_resolve_by_id = True,
                legacy_object = False,
                one_per_tenant = False,
                exportable = True,
                rules = sailpoint.beta.models.config_object_rules.Config Object Rules(
                    take_from_target_rules = [
                        sailpoint.beta.models.config_object_rule.Config Object Rule(
                            path = '$.enabled', 
                            value = null, 
                            modes = [RESTORE, PROMOTE], )
                        ], 
                    default_rules = [
                        sailpoint.beta.models.config_object_rule.Config Object Rule(
                            path = '$.enabled', 
                            modes = [RESTORE, PROMOTE], )
                        ], 
                    editable = True, )
            )
        else:
            return SpConfigObject(
        )
        """

    def testSpConfigObject(self):
        """Test SpConfigObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
