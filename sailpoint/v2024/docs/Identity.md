# Identity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**alias** | **str** | Alternate unique identifier for the identity | [optional] 
**email_address** | **str** | The email address of the identity | [optional] 
**processing_state** | **str** | The processing state of the identity | [optional] 
**identity_status** | **str** | The identity&#39;s status in the system | [optional] 
**manager_ref** | [**IdentityDtoManagerRef**](IdentityDtoManagerRef.md) |  | [optional] 
**is_manager** | **bool** | Whether this identity is a manager of another identity | [optional] [default to False]
**last_refresh** | **datetime** | The last time the identity was refreshed by the system | [optional] 
**attributes** | **object** | A map with the identity attributes for the identity | [optional] 
**lifecycle_state** | [**IdentityDtoLifecycleState**](IdentityDtoLifecycleState.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.identity import Identity

# TODO update the JSON string below
json = "{}"
# create an instance of Identity from a JSON string
identity_instance = Identity.from_json(json)
# print the JSON string representation of the object
print(Identity.to_json())

# convert the object into a dict
identity_dict = identity_instance.to_dict()
# create an instance of Identity from a dict
identity_from_dict = Identity.from_dict(identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


