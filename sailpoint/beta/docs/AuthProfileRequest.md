# AuthProfileRequest


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
from sailpoint.beta.models.auth_profile_request import AuthProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProfileRequest from a JSON string
auth_profile_request_instance = AuthProfileRequest.from_json(json)
# print the JSON string representation of the object
print AuthProfileRequest.to_json()

# convert the object into a dict
auth_profile_request_dict = auth_profile_request_instance.to_dict()
# create an instance of AuthProfileRequest from a dict
auth_profile_request_form_dict = auth_profile_request.from_dict(auth_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


