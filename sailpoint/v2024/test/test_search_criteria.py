# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.search_criteria import SearchCriteria

class TestSearchCriteria(unittest.TestCase):
    """SearchCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchCriteria:
        """Test SearchCriteria
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchCriteria`
        """
        model = SearchCriteria()
        if include_optional:
            return SearchCriteria(
                indices = [entitlements],
                filters = {status={type=TERMS, terms=[active, inactive]}},
                query = sailpoint.v2024.models.search_criteria_query.SearchCriteria_query(),
                query_type = 'TEXT',
                text_query = sailpoint.v2024.models.search_criteria_text_query.SearchCriteria_textQuery(
                    terms = [admin, user], 
                    fields = [role, name], 
                    match_any = True, ),
                include_nested = True,
                sort = [name:asc, createdAt:desc],
                search_after = [12345, 67890]
            )
        else:
            return SearchCriteria(
                indices = [entitlements],
        )
        """

    def testSearchCriteria(self):
        """Test SearchCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
