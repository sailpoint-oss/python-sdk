# RoleMetadataBulkUpdateByQueryRequest

Bulk update by query request of Role metadata. The maximum meta data values that one single role assigned can not exceed 25. Custom metadata need suit licensed. For more information about the query could refer to  [V3 API Perform Search](https://developer.sailpoint.com/docs/api/v3/search-post)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | query the identities to be updated | 
**operation** | **str** | The operation to be performed | 
**replace_scope** | **str** | The choice of update scope. | [optional] 
**values** | [**List[RoleMetadataBulkUpdateByQueryRequestValuesInner]**](RoleMetadataBulkUpdateByQueryRequestValuesInner.md) | The metadata to be updated, including attribute key and value. | 

## Example

```python
from sailpoint.v2024.models.role_metadata_bulk_update_by_query_request import RoleMetadataBulkUpdateByQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMetadataBulkUpdateByQueryRequest from a JSON string
role_metadata_bulk_update_by_query_request_instance = RoleMetadataBulkUpdateByQueryRequest.from_json(json)
# print the JSON string representation of the object
print(RoleMetadataBulkUpdateByQueryRequest.to_json())

# convert the object into a dict
role_metadata_bulk_update_by_query_request_dict = role_metadata_bulk_update_by_query_request_instance.to_dict()
# create an instance of RoleMetadataBulkUpdateByQueryRequest from a dict
role_metadata_bulk_update_by_query_request_from_dict = RoleMetadataBulkUpdateByQueryRequest.from_dict(role_metadata_bulk_update_by_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


