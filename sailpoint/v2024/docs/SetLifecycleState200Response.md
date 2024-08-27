# SetLifecycleState200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_activity_id** | **str** | ID of the IdentityRequest object that is generated when the workflow launches. To follow the IdentityRequest, you can provide this ID with a [Get Account Activity request](https://developer.sailpoint.com/docs/api/v3/get-account-activity/). The response will contain relevant information about the IdentityRequest, such as its status. | [optional] 

## Example

```python
from sailpoint.v2024.models.set_lifecycle_state200_response import SetLifecycleState200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetLifecycleState200Response from a JSON string
set_lifecycle_state200_response_instance = SetLifecycleState200Response.from_json(json)
# print the JSON string representation of the object
print(SetLifecycleState200Response.to_json())

# convert the object into a dict
set_lifecycle_state200_response_dict = set_lifecycle_state200_response_instance.to_dict()
# create an instance of SetLifecycleState200Response from a dict
set_lifecycle_state200_response_from_dict = SetLifecycleState200Response.from_dict(set_lifecycle_state200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


