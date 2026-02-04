import unittest

import sailpoint.beta
import sailpoint.v3
import sailpoint.v2024
import sailpoint.v2026
from sailpoint.configuration import Configuration, ConfigurationParams
from sailpoint.paginator import Paginator
from sailpoint.v3.models.search import Search


class TestPythonSDK(unittest.TestCase):

    configuration = Configuration()
    v3_api_client = sailpoint.v3.ApiClient(configuration)
    beta_api_client = sailpoint.beta.ApiClient(configuration)
    configuration.experimental = True
    v2024_api_client = sailpoint.v2024.ApiClient(configuration)
    v2026_api_client = sailpoint.v2026.ApiClient(configuration)


    def test_manual_configuration(self):
        configurationParams = ConfigurationParams()
        configurationParams.base_url = "https://localhost:8080"
        configurationParams.client_id = "client_id"
        configurationParams.client_secret = "client_secret"
        configuration = Configuration(configurationParams)

        self.assertEqual(configuration.base_url, "https://localhost:8080")
        self.assertEqual(configuration.client_id, "client_id")
        self.assertEqual(configuration.client_secret, "client_secret")

    def test_v3_accounts(self):
        accounts = sailpoint.v3.AccountsApi(self.v3_api_client).list_accounts_with_http_info()
        self.assertIsNotNone(accounts.data)
        self.assertEqual(200, accounts.status_code)

    def test_search_pagination(self):
        search = Search()
        search.indices = ['identities']
        search.query = { 'query': '*' }
        search.sort = ['-name']

        search_results = Paginator.paginate_search_with_http_info(sailpoint.v3.SearchApi(self.v3_api_client), search, 10, 100)

        self.assertIsNotNone(search_results)
        self.assertEqual(100,len(search_results.data))
        self.assertEqual(200,search_results.status_code)

    def test_list_transforms(self):
        transforms = sailpoint.v3.TransformsApi(self.v3_api_client).list_transforms_with_http_info()
        self.assertIsNotNone(transforms.data)
        self.assertEqual(200, transforms.status_code)
    
    def test_pagination(self):
        accounts = Paginator.paginate(sailpoint.v3.AccountsApi(self.v3_api_client).list_accounts_with_http_info, 100, limit=10)
        self.assertIsNotNone(accounts.data)
        self.assertEqual(100, len(accounts.data))
        self.assertEqual(200, accounts.status_code)

    def test_list_accounts_beta(self):
        accounts = sailpoint.beta.AccountsApi(self.beta_api_client).list_accounts_with_http_info()
        self.assertIsNotNone(accounts.data)
        self.assertEqual(200, accounts.status_code)
    
    def test_list_connectors_beta(self):
        connectors = sailpoint.beta.ConnectorsApi(self.beta_api_client).get_connector_list_with_http_info()
        self.assertIsNotNone(connectors.data)
        self.assertEqual(200, connectors.status_code)
    
    def test_list_sources_beta(self):
        sources = sailpoint.beta.SourcesApi(self.beta_api_client).list_sources_with_http_info()
        self.assertIsNotNone(sources.data)
        self.assertEqual(200, sources.status_code)
    
    def test_pagination_with_beta_endpoint(self):
        identity_profiles = Paginator.paginate(sailpoint.beta.IdentityProfilesApi(self.beta_api_client).list_identity_profiles_with_http_info, 2, limit=1)
        self.assertIsNotNone(identity_profiles.data)
        self.assertEqual(200, identity_profiles.status_code)
        self.assertEqual(2, len(identity_profiles.data))
    
    def test_list_identities_with_v2024_endpoint(self):
        identities = sailpoint.v2024.IdentitiesApi(self.v2024_api_client).list_identities_with_http_info()
        self.assertIsNotNone(identities.data)
        self.assertEqual(200, identities.status_code)

    def test_list_identities_with_v2026_endpoint(self):
        tasks = sailpoint.v2026.TaskManagementApi(self.v2026_api_client).get_task_status_list_with_http_info()
        self.assertIsNotNone(tasks.data)
        self.assertEqual(200, tasks.status_code)


class TestLenientEnumsV2025(unittest.TestCase):
    """
    Validate that enum refs use Union[EnumType, str] so unknown values from the API
    are accepted as plain strings (lenient enum validation).
    Uses RequestedItemStatus and RequestedItemStatusRequestState as the main example.
    """

    def test_requested_item_status_accepts_known_state_enum(self):
        """Known state value is coerced to RequestedItemStatusRequestState enum member."""
        from sailpoint.v2025.models.requested_item_status import RequestedItemStatus
        from sailpoint.v2025.models.requested_item_status_request_state import RequestedItemStatusRequestState

        obj = RequestedItemStatus.model_validate({"state": "EXECUTING"})
        self.assertIsNotNone(obj.state)
        self.assertEqual(obj.state, RequestedItemStatusRequestState.EXECUTING)

    def test_requested_item_status_accepts_unknown_state_as_str(self):
        """Unknown state value is accepted as plain str (lenient enum)."""
        from sailpoint.v2025.models.requested_item_status import RequestedItemStatus

        unknown_state = "FUTURE_STATE_NOT_IN_SPEC"
        obj = RequestedItemStatus.model_validate({"state": unknown_state})
        self.assertIsNotNone(obj.state)
        self.assertEqual(obj.state, unknown_state)
        self.assertIsInstance(obj.state, str)

    def test_requested_item_status_accepts_known_request_type_enum(self):
        """Known request_type value is coerced to AccessRequestType enum member."""
        from sailpoint.v2025.models.requested_item_status import RequestedItemStatus
        from sailpoint.v2025.models.access_request_type import AccessRequestType

        obj = RequestedItemStatus.model_validate({"requestType": "GRANT_ACCESS"})
        self.assertIsNotNone(obj.request_type)
        self.assertEqual(obj.request_type, AccessRequestType.GRANT_ACCESS)

    def test_requested_item_status_accepts_unknown_request_type_as_str(self):
        """Unknown request_type value is accepted as plain str (lenient enum)."""
        from sailpoint.v2025.models.requested_item_status import RequestedItemStatus

        unknown_type = "FUTURE_REQUEST_TYPE"
        obj = RequestedItemStatus.model_validate({"requestType": unknown_type})
        self.assertIsNotNone(obj.request_type)
        self.assertEqual(obj.request_type, unknown_type)
        self.assertIsInstance(obj.request_type, str)

    def test_requested_item_status_unknown_state_round_trips_in_dict(self):
        """Unknown state serializes and deserializes correctly (e.g. for API responses)."""
        from sailpoint.v2025.models.requested_item_status import RequestedItemStatus

        unknown_state = "PENDING_NEW_BACKEND"
        obj = RequestedItemStatus.model_validate({"state": unknown_state})
        d = obj.model_dump(by_alias=True)
        self.assertIn("state", d)
        self.assertEqual(d["state"], unknown_state)
        obj2 = RequestedItemStatus.model_validate(d)
        self.assertEqual(obj2.state, unknown_state)


if __name__ == '__main__':
    unittest.main()
