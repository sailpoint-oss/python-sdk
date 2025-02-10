import unittest
import sailpoint.v2024
import sailpoint.v3
import sailpoint.beta
from sailpoint.v3.models.search import Search
from sailpoint.configuration import Configuration, ConfigurationParams
from sailpoint.paginator import Paginator

class TestPythonSDK(unittest.TestCase):

    configuration = Configuration()
    v3_api_client = sailpoint.v3.ApiClient(configuration)
    beta_api_client = sailpoint.beta.ApiClient(configuration)
    configuration.experimental = True
    v2024_api_client = sailpoint.v2024.ApiClient(configuration)


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

if __name__ == '__main__':
    unittest.main()
