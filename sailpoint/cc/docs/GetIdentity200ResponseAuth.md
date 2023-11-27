# GetIdentity200ResponseAuth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**encryption** | **str** |  | [optional] 

## Example

```python
from sailpoint.cc.models.get_identity200_response_auth import GetIdentity200ResponseAuth

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentity200ResponseAuth from a JSON string
get_identity200_response_auth_instance = GetIdentity200ResponseAuth.from_json(json)
# print the JSON string representation of the object
print GetIdentity200ResponseAuth.to_json()

# convert the object into a dict
get_identity200_response_auth_dict = get_identity200_response_auth_instance.to_dict()
# create an instance of GetIdentity200ResponseAuth from a dict
get_identity200_response_auth_form_dict = get_identity200_response_auth.from_dict(get_identity200_response_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


