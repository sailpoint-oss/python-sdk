# GetPersonalAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the personal access token (to be used as the username for Basic Auth). | 
**name** | **str** | The name of the personal access token. Cannot be the same as other personal access tokens owned by a user. | 
**scope** | **List[str]** | Scopes of the personal  access token. | 
**owner** | [**PatOwner**](PatOwner.md) |  | 
**created** | **datetime** | The date and time, down to the millisecond, when this personal access token was created. | 
**last_used** | **datetime** | The date and time, down to the millisecond, when this personal access token was last used to generate an access token. This timestamp does not get updated on every PAT usage, but only once a day. This property can be useful for identifying which PATs are no longer actively used and can be removed. | [optional] 
**managed** | **bool** | If true, this token is managed by the SailPoint platform, and is not visible in the user interface. For example, Workflows will create managed personal access tokens for users who create workflows. | [optional] [default to False]

## Example

```python
from sailpoint.v3.models.get_personal_access_token_response import GetPersonalAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonalAccessTokenResponse from a JSON string
get_personal_access_token_response_instance = GetPersonalAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print GetPersonalAccessTokenResponse.to_json()

# convert the object into a dict
get_personal_access_token_response_dict = get_personal_access_token_response_instance.to_dict()
# create an instance of GetPersonalAccessTokenResponse from a dict
get_personal_access_token_response_form_dict = get_personal_access_token_response.from_dict(get_personal_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


