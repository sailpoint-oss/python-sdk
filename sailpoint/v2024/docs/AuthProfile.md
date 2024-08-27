# AuthProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Authentication Profile name. | [optional] 
**off_network** | **bool** | Use it to block access from off network. | [optional] [default to False]
**untrusted_geography** | **bool** | Use it to block access from untrusted geoographies. | [optional] [default to False]
**application_id** | **str** | Application ID. | [optional] 
**application_name** | **str** | Application name. | [optional] 
**type** | **str** | Type of the Authentication Profile. | [optional] 
**strong_auth_login** | **bool** | Use it to enable strong authentication. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.auth_profile import AuthProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProfile from a JSON string
auth_profile_instance = AuthProfile.from_json(json)
# print the JSON string representation of the object
print(AuthProfile.to_json())

# convert the object into a dict
auth_profile_dict = auth_profile_instance.to_dict()
# create an instance of AuthProfile from a dict
auth_profile_from_dict = AuthProfile.from_dict(auth_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


