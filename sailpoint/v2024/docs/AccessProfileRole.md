# AccessProfileRole

Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**owner** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**revocable** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_role import AccessProfileRole

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileRole from a JSON string
access_profile_role_instance = AccessProfileRole.from_json(json)
# print the JSON string representation of the object
print AccessProfileRole.to_json()

# convert the object into a dict
access_profile_role_dict = access_profile_role_instance.to_dict()
# create an instance of AccessProfileRole from a dict
access_profile_role_form_dict = access_profile_role.from_dict(access_profile_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


