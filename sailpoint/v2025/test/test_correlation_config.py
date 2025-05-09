# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.correlation_config import CorrelationConfig

class TestCorrelationConfig(unittest.TestCase):
    """CorrelationConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CorrelationConfig:
        """Test CorrelationConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CorrelationConfig`
        """
        model = CorrelationConfig()
        if include_optional:
            return CorrelationConfig(
                id = '2c9180835d191a86015d28455b4a2329',
                name = 'Source [source] Account Correlation',
                attribute_assignments = [
                    sailpoint.v2025.models.correlation_config_attribute_assignments_inner.CorrelationConfig_attributeAssignments_inner(
                        property = 'first_name', 
                        value = 'firstName', 
                        operation = 'EQ', 
                        complex = False, 
                        ignore_case = False, 
                        match_mode = 'ANYWHERE', 
                        filter_string = 'first_name == "John"', )
                    ]
            )
        else:
            return CorrelationConfig(
        )
        """

    def testCorrelationConfig(self):
        """Test CorrelationConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
