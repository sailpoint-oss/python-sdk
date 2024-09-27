# RoleMetadataBulkUpdateByIdRequestValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | the key of metadata attribute | 
**values** | **List[str]** | the values of attribute to be updated | 

## Example

```python
from sailpoint.v2024.models.role_metadata_bulk_update_by_id_request_values_inner import RoleMetadataBulkUpdateByIdRequestValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMetadataBulkUpdateByIdRequestValuesInner from a JSON string
role_metadata_bulk_update_by_id_request_values_inner_instance = RoleMetadataBulkUpdateByIdRequestValuesInner.from_json(json)
# print the JSON string representation of the object
print(RoleMetadataBulkUpdateByIdRequestValuesInner.to_json())

# convert the object into a dict
role_metadata_bulk_update_by_id_request_values_inner_dict = role_metadata_bulk_update_by_id_request_values_inner_instance.to_dict()
# create an instance of RoleMetadataBulkUpdateByIdRequestValuesInner from a dict
role_metadata_bulk_update_by_id_request_values_inner_from_dict = RoleMetadataBulkUpdateByIdRequestValuesInner.from_dict(role_metadata_bulk_update_by_id_request_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


