# RoleBulkUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task which is executing the bulk update. This also used in to the bulk-update/** API to track status. | [optional] 
**type** | **str** | Type of the bulk update object. | [optional] 
**status** | **str** | The status of the bulk update request, could also checked by getBulkUpdateStatus API | [optional] 
**created** | **datetime** | Time when the bulk update request was created | [optional] 

## Example

```python
from sailpoint.v2024.models.role_bulk_update_response import RoleBulkUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleBulkUpdateResponse from a JSON string
role_bulk_update_response_instance = RoleBulkUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(RoleBulkUpdateResponse.to_json())

# convert the object into a dict
role_bulk_update_response_dict = role_bulk_update_response_instance.to_dict()
# create an instance of RoleBulkUpdateResponse from a dict
role_bulk_update_response_from_dict = RoleBulkUpdateResponse.from_dict(role_bulk_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


