# TokenAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | MFA Authentication status | [optional] 

## Example

```python
from sailpoint.v3.models.token_auth_response import TokenAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenAuthResponse from a JSON string
token_auth_response_instance = TokenAuthResponse.from_json(json)
# print the JSON string representation of the object
print(TokenAuthResponse.to_json())

# convert the object into a dict
token_auth_response_dict = token_auth_response_instance.to_dict()
# create an instance of TokenAuthResponse from a dict
token_auth_response_from_dict = TokenAuthResponse.from_dict(token_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


