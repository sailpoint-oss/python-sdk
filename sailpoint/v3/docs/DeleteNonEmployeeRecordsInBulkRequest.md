# DeleteNonEmployeeRecordsInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of non-employee ids. | 

## Example

```python
from sailpoint.v3.models.delete_non_employee_records_in_bulk_request import DeleteNonEmployeeRecordsInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNonEmployeeRecordsInBulkRequest from a JSON string
delete_non_employee_records_in_bulk_request_instance = DeleteNonEmployeeRecordsInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteNonEmployeeRecordsInBulkRequest.to_json())

# convert the object into a dict
delete_non_employee_records_in_bulk_request_dict = delete_non_employee_records_in_bulk_request_instance.to_dict()
# create an instance of DeleteNonEmployeeRecordsInBulkRequest from a dict
delete_non_employee_records_in_bulk_request_from_dict = DeleteNonEmployeeRecordsInBulkRequest.from_dict(delete_non_employee_records_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


