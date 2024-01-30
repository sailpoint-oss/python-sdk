# CreatePersonalAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the personal access token (to be used as the username for Basic Auth). | 
**secret** | **str** | The secret of the personal access token (to be used as the password for Basic Auth). | 
**scope** | **List[str]** | Scopes of the personal  access token. | 
**name** | **str** | The name of the personal access token. Cannot be the same as other personal access tokens owned by a user. | 
**owner** | [**PatOwner**](PatOwner.md) |  | 
**created** | **datetime** | The date and time, down to the millisecond, when this personal access token was created. | 

## Example

```python
from sailpoint.v3.models.create_personal_access_token_response import CreatePersonalAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonalAccessTokenResponse from a JSON string
create_personal_access_token_response_instance = CreatePersonalAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print CreatePersonalAccessTokenResponse.to_json()

# convert the object into a dict
create_personal_access_token_response_dict = create_personal_access_token_response_instance.to_dict()
# create an instance of CreatePersonalAccessTokenResponse from a dict
create_personal_access_token_response_form_dict = create_personal_access_token_response.from_dict(create_personal_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


