# NonEmployeeRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee record id. | [optional] 
**account_name** | **str** | Requested identity account name. | [optional] 
**first_name** | **str** | Non-Employee&#39;s first name. | [optional] 
**last_name** | **str** | Non-Employee&#39;s last name. | [optional] 
**email** | **str** | Non-Employee&#39;s email. | [optional] 
**phone** | **str** | Non-Employee&#39;s phone. | [optional] 
**manager** | **str** | The account ID of a valid identity to serve as this non-employee&#39;s manager. | [optional] 
**source_id** | **str** | Non-Employee&#39;s source id. | [optional] 
**data** | **Dict[str, str]** | Attribute blob/bag for a non-employee. | [optional] 
**start_date** | **datetime** | Non-Employee employment start date. | [optional] 
**end_date** | **datetime** | Non-Employee employment end date. | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 

## Example

```python
from beta.models.non_employee_record import NonEmployeeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeRecord from a JSON string
non_employee_record_instance = NonEmployeeRecord.from_json(json)
# print the JSON string representation of the object
print NonEmployeeRecord.to_json()

# convert the object into a dict
non_employee_record_dict = non_employee_record_instance.to_dict()
# create an instance of NonEmployeeRecord from a dict
non_employee_record_form_dict = non_employee_record.from_dict(non_employee_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


