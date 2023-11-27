# CreateOAuthClientRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** | The name of the business the API Client should belong to | [optional] 
**homepage_url** | **str** | The homepage URL associated with the owner of the API Client | [optional] 
**name** | **str** | A human-readable name for the API Client | 
**description** | **str** | A description of the API Client | 
**access_token_validity_seconds** | **int** | The number of seconds an access token generated for this API Client is valid for | 
**refresh_token_validity_seconds** | **int** | The number of seconds a refresh token generated for this API Client is valid for | [optional] 
**redirect_uris** | **List[str]** | A list of the approved redirect URIs. Provide one or more URIs when assigning the AUTHORIZATION_CODE grant type to a new OAuth Client. | [optional] 
**grant_types** | [**List[GrantType]**](GrantType.md) | A list of OAuth 2.0 grant types this API Client can be used with | 
**access_type** | [**AccessType**](AccessType.md) |  | 
**type** | [**ClientType**](ClientType.md) |  | [optional] 
**internal** | **bool** | An indicator of whether the API Client can be used for requests internal within the product. | [optional] 
**enabled** | **bool** | An indicator of whether the API Client is enabled for use | 
**strong_auth_supported** | **bool** | An indicator of whether the API Client supports strong authentication | [optional] 
**claims_supported** | **bool** | An indicator of whether the API Client supports the serialization of SAML claims when used with the authorization_code flow | [optional] 
**scope** | **List[str]** | Scopes of the API Client. If no scope is specified, the client will be created with the default scope \&quot;sp:scopes:all\&quot;. This means the API Client will have all the rights of the owner who created it. | [optional] 

## Example

```python
from sailpoint.v3.models.create_o_auth_client_request import CreateOAuthClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOAuthClientRequest from a JSON string
create_o_auth_client_request_instance = CreateOAuthClientRequest.from_json(json)
# print the JSON string representation of the object
print CreateOAuthClientRequest.to_json()

# convert the object into a dict
create_o_auth_client_request_dict = create_o_auth_client_request_instance.to_dict()
# create an instance of CreateOAuthClientRequest from a dict
create_o_auth_client_request_form_dict = create_o_auth_client_request.from_dict(create_o_auth_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


