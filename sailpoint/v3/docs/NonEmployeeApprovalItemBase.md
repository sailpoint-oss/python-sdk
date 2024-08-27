# NonEmployeeApprovalItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee approval item id | [optional] 
**approver** | [**NonEmployeeIdentityReferenceWithId**](NonEmployeeIdentityReferenceWithId.md) |  | [optional] 
**account_name** | **str** | Requested identity account name | [optional] 
**approval_status** | [**ApprovalStatus**](ApprovalStatus.md) |  | [optional] 
**approval_order** | **float** | Approval order | [optional] 
**comment** | **str** | comment of approver | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_approval_item_base import NonEmployeeApprovalItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeApprovalItemBase from a JSON string
non_employee_approval_item_base_instance = NonEmployeeApprovalItemBase.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeApprovalItemBase.to_json())

# convert the object into a dict
non_employee_approval_item_base_dict = non_employee_approval_item_base_instance.to_dict()
# create an instance of NonEmployeeApprovalItemBase from a dict
non_employee_approval_item_base_from_dict = NonEmployeeApprovalItemBase.from_dict(non_employee_approval_item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


