# RoleBulkDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_ids** | **List[str]** | List of IDs of Roles to be deleted. | 

## Example

```python
from sailpoint.v2024.models.role_bulk_delete_request import RoleBulkDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleBulkDeleteRequest from a JSON string
role_bulk_delete_request_instance = RoleBulkDeleteRequest.from_json(json)
# print the JSON string representation of the object
print RoleBulkDeleteRequest.to_json()

# convert the object into a dict
role_bulk_delete_request_dict = role_bulk_delete_request_instance.to_dict()
# create an instance of RoleBulkDeleteRequest from a dict
role_bulk_delete_request_form_dict = role_bulk_delete_request.from_dict(role_bulk_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


