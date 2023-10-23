# WorkgroupBulkDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of IDs of Governance Groups to be deleted. | [optional] 

## Example

```python
from beta.models.workgroup_bulk_delete_request import WorkgroupBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupBulkDeleteRequest from a JSON string
workgroup_bulk_delete_request_instance = WorkgroupBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print WorkgroupBulkDeleteRequest.to_json()

# convert the object into a dict
workgroup_bulk_delete_request_dict = workgroup_bulk_delete_request_instance.to_dict()
# create an instance of WorkgroupBulkDeleteRequest from a dict
workgroup_bulk_delete_request_form_dict = workgroup_bulk_delete_request.from_dict(workgroup_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


