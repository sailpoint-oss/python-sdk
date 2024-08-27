# AccessItemRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | the access item type. role in this case | [optional] 
**id** | **str** | the access item id | [optional] 
**display_name** | **str** | the role display name | [optional] 
**description** | **str** | the description for the role | [optional] 
**source_name** | **str** | the associated source name if it exists | [optional] 
**remove_date** | **str** | the date the role is no longer assigned to the specified identity | [optional] 
**revocable** | **bool** | indicates whether the role is revocable | 

## Example

```python
from sailpoint.v2024.models.access_item_role_response import AccessItemRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRoleResponse from a JSON string
access_item_role_response_instance = AccessItemRoleResponse.from_json(json)
# print the JSON string representation of the object
print(AccessItemRoleResponse.to_json())

# convert the object into a dict
access_item_role_response_dict = access_item_role_response_instance.to_dict()
# create an instance of AccessItemRoleResponse from a dict
access_item_role_response_from_dict = AccessItemRoleResponse.from_dict(access_item_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


