# NonEmployeeRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Requested identity account name. | 
**first_name** | **str** | Non-Employee&#39;s first name. | 
**last_name** | **str** | Non-Employee&#39;s last name. | 
**email** | **str** | Non-Employee&#39;s email. | 
**phone** | **str** | Non-Employee&#39;s phone. | 
**manager** | **str** | The account ID of a valid identity to serve as this non-employee&#39;s manager. | 
**source_id** | **str** | Non-Employee&#39;s source id. | 
**data** | **Dict[str, str]** | Attribute blob/bag for a non-employee, 10 attributes is the maximum size supported. | [optional] 
**start_date** | **datetime** | Non-Employee employment start date. | 
**end_date** | **datetime** | Non-Employee employment end date. | 

## Example

```python
from v3.models.non_employee_request_body import NonEmployeeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeRequestBody from a JSON string
non_employee_request_body_instance = NonEmployeeRequestBody.from_json(json)
# print the JSON string representation of the object
print NonEmployeeRequestBody.to_json()

# convert the object into a dict
non_employee_request_body_dict = non_employee_request_body_instance.to_dict()
# create an instance of NonEmployeeRequestBody from a dict
non_employee_request_body_form_dict = non_employee_request_body.from_dict(non_employee_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


