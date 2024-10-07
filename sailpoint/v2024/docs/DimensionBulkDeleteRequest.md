# DimensionBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_ids** | **List[str]** | List of IDs of Dimensions to be deleted. | 

## Example

```python
from sailpoint.v2024.models.dimension_bulk_delete_request import DimensionBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionBulkDeleteRequest from a JSON string
dimension_bulk_delete_request_instance = DimensionBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(DimensionBulkDeleteRequest.to_json())

# convert the object into a dict
dimension_bulk_delete_request_dict = dimension_bulk_delete_request_instance.to_dict()
# create an instance of DimensionBulkDeleteRequest from a dict
dimension_bulk_delete_request_from_dict = DimensionBulkDeleteRequest.from_dict(dimension_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


