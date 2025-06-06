# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.list_form_element_data_by_element_id_response import ListFormElementDataByElementIDResponse

class TestListFormElementDataByElementIDResponse(unittest.TestCase):
    """ListFormElementDataByElementIDResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListFormElementDataByElementIDResponse:
        """Test ListFormElementDataByElementIDResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFormElementDataByElementIDResponse`
        """
        model = ListFormElementDataByElementIDResponse()
        if include_optional:
            return ListFormElementDataByElementIDResponse(
                results = {"results":[{"label":"Alfred 255e71dfc6e","subLabel":"Alfred.255e71dfc6e@testmail.identitysoon.com","value":"2c918084821847c5018227ced2e16676"},{"label":"Alize eba9d4cd27da","subLabel":"Alize.eba9d4cd27da@testmail.identitysoon.com","value":"2c918084821847c5018227ced2f1667c"},{"label":"Antonina 01f69c3ea","subLabel":"Antonina.01f69c3ea@testmail.identitysoon.com","value":"2c918084821847c5018227ced2f9667e"},{"label":"Ardella 21e78ce155","subLabel":"Ardella.21e78ce155@testmail.identitysoon.com","value":"2c918084821847c5018227ced2e6667a"},{"label":"Arnaldo d8582b6e17","subLabel":"Arnaldo.d8582b6e17@testmail.identitysoon.com","value":"2c918084821847c5018227ced3426686"},{"label":"Aurelia admin24828","subLabel":"Aurelia.admin24828@testmail.identitysoon.com","value":"2c918084821847c5018227ced2e16674"},{"label":"Barbara 72ca418fdd","subLabel":"Barbara.72ca418fdd@testmail.identitysoon.com","value":"2c918084821847c5018227ced2fb6680"},{"label":"Barbara ee1a2436ee","subLabel":"Barbara.ee1a2436ee@testmail.identitysoon.com","value":"2c918084821847c5018227ced2e56678"},{"label":"Baylee 652d72432f3","subLabel":"Baylee.652d72432f3@testmail.identitysoon.com","value":"2c91808582184782018227ced28b6aee"},{"label":"Brock e76b56ae4d49","subLabel":"Brock.e76b56ae4d49@testmail.identitysoon.com","value":"2c91808582184782018227ced28b6aef"}]}
            )
        else:
            return ListFormElementDataByElementIDResponse(
        )
        """

    def testListFormElementDataByElementIDResponse(self):
        """Test ListFormElementDataByElementIDResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
