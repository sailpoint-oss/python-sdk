# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.client_log_configuration_expiration import ClientLogConfigurationExpiration

class TestClientLogConfigurationExpiration(unittest.TestCase):
    """ClientLogConfigurationExpiration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientLogConfigurationExpiration:
        """Test ClientLogConfigurationExpiration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientLogConfigurationExpiration`
        """
        model = ClientLogConfigurationExpiration()
        if include_optional:
            return ClientLogConfigurationExpiration(
                client_id = '3a38a51992e8445ab51a549c0a70ee66',
                expiration = '2024-11-06T01:31:08.013164Z',
                root_level = 'INFO',
                log_levels = INFO
            )
        else:
            return ClientLogConfigurationExpiration(
                root_level = 'INFO',
        )
        """

    def testClientLogConfigurationExpiration(self):
        """Test ClientLogConfigurationExpiration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()