# CreatePersonalAccessTokenRequest

Object for specifying the name of a personal access token to create

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the personal access token (PAT) to be created. Cannot be the same as another PAT owned by the user for whom this PAT is being created. | 
**scope** | **List[str]** | Scopes of the personal access token. If no scope is specified, the token will be created with the default scope \&quot;sp:scopes:all\&quot;. This means the personal access token will have all the rights of the owner who created it. | [optional] 

## Example

```python
from sailpoint.beta.models.create_personal_access_token_request import CreatePersonalAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonalAccessTokenRequest from a JSON string
create_personal_access_token_request_instance = CreatePersonalAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePersonalAccessTokenRequest.to_json())

# convert the object into a dict
create_personal_access_token_request_dict = create_personal_access_token_request_instance.to_dict()
# create an instance of CreatePersonalAccessTokenRequest from a dict
create_personal_access_token_request_from_dict = CreatePersonalAccessTokenRequest.from_dict(create_personal_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


