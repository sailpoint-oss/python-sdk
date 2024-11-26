# RoleGetAllBulkUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task which is executing the bulk update. This also used in to the bulk-update/** API to track status. | [optional] 
**type** | **str** | Type of the bulk update object. | [optional] 
**status** | **str** | The status of the bulk update request, only list unfinished request&#39;s status, the status could also checked by getBulkUpdateStatus API | [optional] 
**created** | **datetime** | Time when the bulk update request was created | [optional] 

## Example

```python
from sailpoint.v2024.models.role_get_all_bulk_update_response import RoleGetAllBulkUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGetAllBulkUpdateResponse from a JSON string
role_get_all_bulk_update_response_instance = RoleGetAllBulkUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RoleGetAllBulkUpdateResponse.to_json())

# convert the object into a dict
role_get_all_bulk_update_response_dict = role_get_all_bulk_update_response_instance.to_dict()
# create an instance of RoleGetAllBulkUpdateResponse from a dict
role_get_all_bulk_update_response_from_dict = RoleGetAllBulkUpdateResponse.from_dict(role_get_all_bulk_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


