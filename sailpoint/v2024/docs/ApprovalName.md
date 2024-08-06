# ApprovalName

Approval Name Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Name of the approval | [optional] 
**locale** | **str** | What locale the name of the approval is using | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_name import ApprovalName

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalName from a JSON string
approval_name_instance = ApprovalName.from_json(json)
# print the JSON string representation of the object
print ApprovalName.to_json()

# convert the object into a dict
approval_name_dict = approval_name_instance.to_dict()
# create an instance of ApprovalName from a dict
approval_name_form_dict = approval_name.from_dict(approval_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


