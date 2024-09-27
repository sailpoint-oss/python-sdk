# RoleMetadataBulkUpdateByIdRequest

This API initialize a Bulk update by Id request of Role metadata. The maximum role count in a single update request is 3000. The maximum meta data values that one single role assigned can not exceed 25. Custom metadata need suit licensed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | Roles&#39; Id to be updated | 
**operation** | **str** | The operation to be performed | 
**replace_scope** | **str** | The choice of update scope. | [optional] 
**values** | [**List[RoleMetadataBulkUpdateByIdRequestValuesInner]**](RoleMetadataBulkUpdateByIdRequestValuesInner.md) | The metadata to be updated, including attribute key and value. | 

## Example

```python
from sailpoint.v2024.models.role_metadata_bulk_update_by_id_request import RoleMetadataBulkUpdateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMetadataBulkUpdateByIdRequest from a JSON string
role_metadata_bulk_update_by_id_request_instance = RoleMetadataBulkUpdateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(RoleMetadataBulkUpdateByIdRequest.to_json())

# convert the object into a dict
role_metadata_bulk_update_by_id_request_dict = role_metadata_bulk_update_by_id_request_instance.to_dict()
# create an instance of RoleMetadataBulkUpdateByIdRequest from a dict
role_metadata_bulk_update_by_id_request_from_dict = RoleMetadataBulkUpdateByIdRequest.from_dict(role_metadata_bulk_update_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


