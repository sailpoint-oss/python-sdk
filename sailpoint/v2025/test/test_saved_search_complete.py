# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.saved_search_complete import SavedSearchComplete

class TestSavedSearchComplete(unittest.TestCase):
    """SavedSearchComplete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedSearchComplete:
        """Test SavedSearchComplete
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavedSearchComplete`
        """
        model = SavedSearchComplete()
        if include_optional:
            return SavedSearchComplete(
                file_name = 'Modified.zip',
                owner_email = 'test@sailpoint.com',
                owner_name = 'Cloud Support',
                query = 'modified:[now-7y/d TO now]',
                search_name = 'Modified Activity',
                search_results = sailpoint.v2025.models.saved_search_complete_search_results.SavedSearchComplete_searchResults(
                    account = sailpoint.v2025.models.saved_search_complete_search_results_account.SavedSearchComplete_searchResults_Account(
                        count = '3', 
                        noun = 'accounts', 
                        preview = [
                            []
                            ], ), 
                    entitlement = sailpoint.v2025.models.saved_search_complete_search_results_entitlement.SavedSearchComplete_searchResults_Entitlement(
                        count = '2', 
                        noun = 'entitlements', 
                        preview = [
                            []
                            ], ), 
                    identity = sailpoint.v2025.models.saved_search_complete_search_results_identity.SavedSearchComplete_searchResults_Identity(
                        count = '2', 
                        noun = 'identities', 
                        preview = [
                            []
                            ], ), ),
                signed_s3_url = 'https://sptcbu-org-data-useast1.s3.amazonaws.com/arsenal-john/reports/Events%20Export.2020-05-06%2018%2759%20GMT.3e580592-86e4-4953-8aea-49e6ef20a086.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200506T185919Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=AKIAV5E54XOGTS4Q4L7A%2F20200506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2e732bb97a12a1fd8a215613e3c31fcdae8ba1fb6a25916843ab5b51d2ddefbc'
            )
        else:
            return SavedSearchComplete(
                file_name = 'Modified.zip',
                owner_email = 'test@sailpoint.com',
                owner_name = 'Cloud Support',
                query = 'modified:[now-7y/d TO now]',
                search_name = 'Modified Activity',
                search_results = sailpoint.v2025.models.saved_search_complete_search_results.SavedSearchComplete_searchResults(
                    account = sailpoint.v2025.models.saved_search_complete_search_results_account.SavedSearchComplete_searchResults_Account(
                        count = '3', 
                        noun = 'accounts', 
                        preview = [
                            []
                            ], ), 
                    entitlement = sailpoint.v2025.models.saved_search_complete_search_results_entitlement.SavedSearchComplete_searchResults_Entitlement(
                        count = '2', 
                        noun = 'entitlements', 
                        preview = [
                            []
                            ], ), 
                    identity = sailpoint.v2025.models.saved_search_complete_search_results_identity.SavedSearchComplete_searchResults_Identity(
                        count = '2', 
                        noun = 'identities', 
                        preview = [
                            []
                            ], ), ),
                signed_s3_url = 'https://sptcbu-org-data-useast1.s3.amazonaws.com/arsenal-john/reports/Events%20Export.2020-05-06%2018%2759%20GMT.3e580592-86e4-4953-8aea-49e6ef20a086.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200506T185919Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=AKIAV5E54XOGTS4Q4L7A%2F20200506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2e732bb97a12a1fd8a215613e3c31fcdae8ba1fb6a25916843ab5b51d2ddefbc',
        )
        """

    def testSavedSearchComplete(self):
        """Test SavedSearchComplete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
