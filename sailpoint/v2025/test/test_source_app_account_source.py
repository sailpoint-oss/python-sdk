# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.source_app_account_source import SourceAppAccountSource

class TestSourceAppAccountSource(unittest.TestCase):
    """SourceAppAccountSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceAppAccountSource:
        """Test SourceAppAccountSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceAppAccountSource`
        """
        model = SourceAppAccountSource()
        if include_optional:
            return SourceAppAccountSource(
                id = '2c9180827ca885d7017ca8ce28a000eb',
                type = 'SOURCE',
                name = 'ODS-AD-Source',
                use_for_password_management = False,
                password_policies = [{type=PASSWORD_POLICY, id=006a072ecc6647f68bba9f4a4ad34649, name=Password Policy 1}]
            )
        else:
            return SourceAppAccountSource(
        )
        """

    def testSourceAppAccountSource(self):
        """Test SourceAppAccountSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
