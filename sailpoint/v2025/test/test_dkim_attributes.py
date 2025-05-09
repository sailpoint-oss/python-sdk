# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.dkim_attributes import DkimAttributes

class TestDkimAttributes(unittest.TestCase):
    """DkimAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DkimAttributes:
        """Test DkimAttributes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DkimAttributes`
        """
        model = DkimAttributes()
        if include_optional:
            return DkimAttributes(
                id = '123b45b0-aaaa-bbbb-a7db-123456a56abc',
                address = 'BobSmith@sailpoint.com',
                dkim_enabled = True,
                dkim_tokens = [uq1m3jjk25ckd3whl4n7y46c56r5l6aq, u7pm38jky9ckdawhlsn7y4dcj6f5lpgq, uhpm3jjkjjckdkwhlqn7yw6cjer5tpay],
                dkim_verification_status = 'Success'
            )
        else:
            return DkimAttributes(
        )
        """

    def testDkimAttributes(self):
        """Test DkimAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
