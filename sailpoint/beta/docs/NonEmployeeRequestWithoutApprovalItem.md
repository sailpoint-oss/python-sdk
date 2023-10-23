# NonEmployeeRequestWithoutApprovalItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee request id. | [optional] 
**requester** | [**IdentityReferenceWithId**](IdentityReferenceWithId.md) |  | [optional] 
**account_name** | **str** | Requested identity account name. | [optional] 
**first_name** | **str** | Non-Employee&#39;s first name. | [optional] 
**last_name** | **str** | Non-Employee&#39;s last name. | [optional] 
**email** | **str** | Non-Employee&#39;s email. | [optional] 
**phone** | **str** | Non-Employee&#39;s phone. | [optional] 
**manager** | **str** | The account ID of a valid identity to serve as this non-employee&#39;s manager. | [optional] 
**non_employee_source** | [**NonEmployeeSourceLiteWithSchemaAttributes**](NonEmployeeSourceLiteWithSchemaAttributes.md) |  | [optional] 
**data** | **Dict[str, str]** | Attribute blob/bag for a non-employee. | [optional] 
**approval_status** | [**ApprovalStatus**](ApprovalStatus.md) |  | [optional] 
**comment** | **str** | comment of requester | [optional] 
**completion_date** | **datetime** | When the request was completely approved. | [optional] 
**start_date** | **date** | Non-Employee employment start date. | [optional] 
**end_date** | **date** | Non-Employee employment end date. | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 

## Example

```python
from beta.models.non_employee_request_without_approval_item import NonEmployeeRequestWithoutApprovalItem

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeRequestWithoutApprovalItem from a JSON string
non_employee_request_without_approval_item_instance = NonEmployeeRequestWithoutApprovalItem.from_json(json)
# print the JSON string representation of the object
print NonEmployeeRequestWithoutApprovalItem.to_json()

# convert the object into a dict
non_employee_request_without_approval_item_dict = non_employee_request_without_approval_item_instance.to_dict()
# create an instance of NonEmployeeRequestWithoutApprovalItem from a dict
non_employee_request_without_approval_item_form_dict = non_employee_request_without_approval_item.from_dict(non_employee_request_without_approval_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


