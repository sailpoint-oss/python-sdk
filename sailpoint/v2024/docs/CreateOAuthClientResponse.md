# CreateOAuthClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the OAuth client | 
**secret** | **str** | Secret of the OAuth client (This field is only returned on the intial create call.) | 
**business_name** | **str** | The name of the business the API Client should belong to | 
**homepage_url** | **str** | The homepage URL associated with the owner of the API Client | 
**name** | **str** | A human-readable name for the API Client | 
**description** | **str** | A description of the API Client | 
**access_token_validity_seconds** | **int** | The number of seconds an access token generated for this API Client is valid for | 
**refresh_token_validity_seconds** | **int** | The number of seconds a refresh token generated for this API Client is valid for | 
**redirect_uris** | **List[str]** | A list of the approved redirect URIs used with the authorization_code flow | 
**grant_types** | [**List[GrantType]**](GrantType.md) | A list of OAuth 2.0 grant types this API Client can be used with | 
**access_type** | [**AccessType**](AccessType.md) |  | 
**type** | [**ClientType**](ClientType.md) |  | 
**internal** | **bool** | An indicator of whether the API Client can be used for requests internal to IDN | 
**enabled** | **bool** | An indicator of whether the API Client is enabled for use | 
**strong_auth_supported** | **bool** | An indicator of whether the API Client supports strong authentication | 
**claims_supported** | **bool** | An indicator of whether the API Client supports the serialization of SAML claims when used with the authorization_code flow | 
**created** | **datetime** | The date and time, down to the millisecond, when the API Client was created | 
**modified** | **datetime** | The date and time, down to the millisecond, when the API Client was last updated | 
**scope** | **List[str]** | Scopes of the API Client. | 

## Example

```python
from sailpoint.v2024.models.create_o_auth_client_response import CreateOAuthClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOAuthClientResponse from a JSON string
create_o_auth_client_response_instance = CreateOAuthClientResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOAuthClientResponse.to_json())

# convert the object into a dict
create_o_auth_client_response_dict = create_o_auth_client_response_instance.to_dict()
# create an instance of CreateOAuthClientResponse from a dict
create_o_auth_client_response_from_dict = CreateOAuthClientResponse.from_dict(create_o_auth_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


