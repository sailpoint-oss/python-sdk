# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.iai_access_request_recommendations_api import IAIAccessRequestRecommendationsApi


class TestIAIAccessRequestRecommendationsApi(unittest.TestCase):
    """IAIAccessRequestRecommendationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IAIAccessRequestRecommendationsApi()

    def tearDown(self) -> None:
        pass

    def test_add_access_request_recommendations_ignored_item(self) -> None:
        """Test case for add_access_request_recommendations_ignored_item

        Ignore access request recommendation
        """
        pass

    def test_add_access_request_recommendations_requested_item(self) -> None:
        """Test case for add_access_request_recommendations_requested_item

        Accept access request recommendation
        """
        pass

    def test_add_access_request_recommendations_viewed_item(self) -> None:
        """Test case for add_access_request_recommendations_viewed_item

        Mark viewed access request recommendations
        """
        pass

    def test_add_access_request_recommendations_viewed_items(self) -> None:
        """Test case for add_access_request_recommendations_viewed_items

        Bulk mark viewed access request recommendations
        """
        pass

    def test_get_access_request_recommendations(self) -> None:
        """Test case for get_access_request_recommendations

        Identity access request recommendations
        """
        pass

    def test_get_access_request_recommendations_ignored_items(self) -> None:
        """Test case for get_access_request_recommendations_ignored_items

        List ignored access request recommendations
        """
        pass

    def test_get_access_request_recommendations_requested_items(self) -> None:
        """Test case for get_access_request_recommendations_requested_items

        List accepted access request recommendations
        """
        pass

    def test_get_access_request_recommendations_viewed_items(self) -> None:
        """Test case for get_access_request_recommendations_viewed_items

        List viewed access request recommendations
        """
        pass


if __name__ == '__main__':
    unittest.main()
