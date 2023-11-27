# BulkDeleteWorkGroupsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from sailpoint.v2.models.bulk_delete_work_groups_request import BulkDeleteWorkGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteWorkGroupsRequest from a JSON string
bulk_delete_work_groups_request_instance = BulkDeleteWorkGroupsRequest.from_json(json)
# print the JSON string representation of the object
print BulkDeleteWorkGroupsRequest.to_json()

# convert the object into a dict
bulk_delete_work_groups_request_dict = bulk_delete_work_groups_request_instance.to_dict()
# create an instance of BulkDeleteWorkGroupsRequest from a dict
bulk_delete_work_groups_request_form_dict = bulk_delete_work_groups_request.from_dict(bulk_delete_work_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


