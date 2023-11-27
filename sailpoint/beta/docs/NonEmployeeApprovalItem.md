# NonEmployeeApprovalItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee approval item id | [optional] 
**approver** | [**IdentityReferenceWithId**](IdentityReferenceWithId.md) |  | [optional] 
**account_name** | **str** | Requested identity account name | [optional] 
**approval_status** | [**ApprovalStatus**](ApprovalStatus.md) |  | [optional] 
**approval_order** | **float** | Approval order | [optional] 
**comment** | **str** | comment of approver | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 
**non_employee_request** | [**NonEmployeeRequestLite**](NonEmployeeRequestLite.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.non_employee_approval_item import NonEmployeeApprovalItem

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeApprovalItem from a JSON string
non_employee_approval_item_instance = NonEmployeeApprovalItem.from_json(json)
# print the JSON string representation of the object
print NonEmployeeApprovalItem.to_json()

# convert the object into a dict
non_employee_approval_item_dict = non_employee_approval_item_instance.to_dict()
# create an instance of NonEmployeeApprovalItem from a dict
non_employee_approval_item_form_dict = non_employee_approval_item.from_dict(non_employee_approval_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


