# NonEmployeeApprovalItemDetail


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
**non_employee_request** | [**NonEmployeeRequestWithoutApprovalItem**](NonEmployeeRequestWithoutApprovalItem.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_approval_item_detail import NonEmployeeApprovalItemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeApprovalItemDetail from a JSON string
non_employee_approval_item_detail_instance = NonEmployeeApprovalItemDetail.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeApprovalItemDetail.to_json())

# convert the object into a dict
non_employee_approval_item_detail_dict = non_employee_approval_item_detail_instance.to_dict()
# create an instance of NonEmployeeApprovalItemDetail from a dict
non_employee_approval_item_detail_from_dict = NonEmployeeApprovalItemDetail.from_dict(non_employee_approval_item_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


