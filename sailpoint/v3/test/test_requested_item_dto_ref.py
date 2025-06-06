# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.models.requested_item_dto_ref import RequestedItemDtoRef

class TestRequestedItemDtoRef(unittest.TestCase):
    """RequestedItemDtoRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestedItemDtoRef:
        """Test RequestedItemDtoRef
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestedItemDtoRef`
        """
        model = RequestedItemDtoRef()
        if include_optional:
            return RequestedItemDtoRef(
                type = 'ACCESS_PROFILE',
                id = '2c9180835d2e5168015d32f890ca1581',
                comment = 'Requesting access profile for John Doe',
                client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1},
                remove_date = '2020-07-11T21:23:15Z',
                account_selection = [
                    sailpoint.v3.models.source_item_ref.SourceItemRef(
                        source_id = 'cb89bc2f1ee6445fbea12224c526ba3a', 
                        accounts = [
                            sailpoint.v3.models.account_item_ref.AccountItemRef(
                                account_uuid = '{fab7119e-004f-4822-9c33-b8d570d6c6a6}', 
                                native_identity = 'CN=Glen 067da3248e914,OU=YOUROU,OU=org-data-service,DC=YOURDC,DC=local', )
                            ], )
                    ]
            )
        else:
            return RequestedItemDtoRef(
                type = 'ACCESS_PROFILE',
                id = '2c9180835d2e5168015d32f890ca1581',
        )
        """

    def testRequestedItemDtoRef(self):
        """Test RequestedItemDtoRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
