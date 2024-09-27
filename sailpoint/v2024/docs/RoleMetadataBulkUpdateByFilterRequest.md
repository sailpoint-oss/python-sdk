# RoleMetadataBulkUpdateByFilterRequest

This API initialize a a Bulk update by filter request of Role metadata. The maximum meta data values that one single role assigned can not exceed 25. Custom metadata need suit licensed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **str** | Filtering is supported for the following fields and operators:  **id** : *eq, in*  **name** : *eq, sw*  **created** : *gt, lt, ge, le*  **modified** : *gt, lt, ge, le*  **owner.id** : *eq, in*  **requestable** : *eq* | 
**operation** | **str** | The operation to be performed | 
**replace_scope** | **str** | The choice of update scope. | [optional] 
**values** | [**List[RoleMetadataBulkUpdateByFilterRequestValuesInner]**](RoleMetadataBulkUpdateByFilterRequestValuesInner.md) | The metadata to be updated, including attribute key and value. | 

## Example

```python
from sailpoint.v2024.models.role_metadata_bulk_update_by_filter_request import RoleMetadataBulkUpdateByFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMetadataBulkUpdateByFilterRequest from a JSON string
role_metadata_bulk_update_by_filter_request_instance = RoleMetadataBulkUpdateByFilterRequest.from_json(json)
# print the JSON string representation of the object
print(RoleMetadataBulkUpdateByFilterRequest.to_json())

# convert the object into a dict
role_metadata_bulk_update_by_filter_request_dict = role_metadata_bulk_update_by_filter_request_instance.to_dict()
# create an instance of RoleMetadataBulkUpdateByFilterRequest from a dict
role_metadata_bulk_update_by_filter_request_from_dict = RoleMetadataBulkUpdateByFilterRequest.from_dict(role_metadata_bulk_update_by_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


