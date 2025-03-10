# Approval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[ApprovalComment]**](ApprovalComment.md) |  | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**owner** | [**ActivityIdentity**](ActivityIdentity.md) |  | [optional] 
**result** | **str** | The result of the approval | [optional] 
**attribute_request** | [**AttributeRequest**](AttributeRequest.md) |  | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.approval import Approval

# TODO update the JSON string below
json = "{}"
# create an instance of Approval from a JSON string
approval_instance = Approval.from_json(json)
# print the JSON string representation of the object
print(Approval.to_json())

# convert the object into a dict
approval_dict = approval_instance.to_dict()
# create an instance of Approval from a dict
approval_from_dict = Approval.from_dict(approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


