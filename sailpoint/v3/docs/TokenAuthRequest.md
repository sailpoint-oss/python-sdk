# TokenAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token value | 
**user_alias** | **str** | User alias from table spt_identity field named &#39;name&#39; | 
**delivery_type** | **str** | Token delivery type | 

## Example

```python
from sailpoint.v3.models.token_auth_request import TokenAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenAuthRequest from a JSON string
token_auth_request_instance = TokenAuthRequest.from_json(json)
# print the JSON string representation of the object
print(TokenAuthRequest.to_json())

# convert the object into a dict
token_auth_request_dict = token_auth_request_instance.to_dict()
# create an instance of TokenAuthRequest from a dict
token_auth_request_from_dict = TokenAuthRequest.from_dict(token_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


