# DeleteNonEmployeeRecordInBulkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of non-employee ids. | 

## Example

```python
from beta.models.delete_non_employee_record_in_bulk_request import DeleteNonEmployeeRecordInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNonEmployeeRecordInBulkRequest from a JSON string
delete_non_employee_record_in_bulk_request_instance = DeleteNonEmployeeRecordInBulkRequest.from_json(json)
# print the JSON string representation of the object
print DeleteNonEmployeeRecordInBulkRequest.to_json()

# convert the object into a dict
delete_non_employee_record_in_bulk_request_dict = delete_non_employee_record_in_bulk_request_instance.to_dict()
# create an instance of DeleteNonEmployeeRecordInBulkRequest from a dict
delete_non_employee_record_in_bulk_request_form_dict = delete_non_employee_record_in_bulk_request.from_dict(delete_non_employee_record_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


