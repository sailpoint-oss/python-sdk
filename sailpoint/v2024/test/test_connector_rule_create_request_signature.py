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

from sailpoint.v2024.models.connector_rule_create_request_signature import ConnectorRuleCreateRequestSignature

class TestConnectorRuleCreateRequestSignature(unittest.TestCase):
    """ConnectorRuleCreateRequestSignature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorRuleCreateRequestSignature:
        """Test ConnectorRuleCreateRequestSignature
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorRuleCreateRequestSignature`
        """
        model = ConnectorRuleCreateRequestSignature()
        if include_optional:
            return ConnectorRuleCreateRequestSignature(
                input = [
                    sailpoint.v2024.models.argument.Argument(
                        name = 'firstName', 
                        description = 'the first name of the identity', 
                        type = 'String', )
                    ],
                output = sailpoint.v2024.models.argument.Argument(
                    name = 'firstName', 
                    description = 'the first name of the identity', 
                    type = 'String', )
            )
        else:
            return ConnectorRuleCreateRequestSignature(
                input = [
                    sailpoint.v2024.models.argument.Argument(
                        name = 'firstName', 
                        description = 'the first name of the identity', 
                        type = 'String', )
                    ],
        )
        """

    def testConnectorRuleCreateRequestSignature(self):
        """Test ConnectorRuleCreateRequestSignature"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()