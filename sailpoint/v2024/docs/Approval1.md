# Approval1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[ApprovalComment2]**](ApprovalComment2.md) |  | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**owner** | [**ActivityIdentity**](ActivityIdentity.md) |  | [optional] 
**result** | **str** | The result of the approval | [optional] 
**attribute_request** | [**AttributeRequest**](AttributeRequest.md) |  | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.approval1 import Approval1

# TODO update the JSON string below
json = "{}"
# create an instance of Approval1 from a JSON string
approval1_instance = Approval1.from_json(json)
# print the JSON string representation of the object
print(Approval1.to_json())

# convert the object into a dict
approval1_dict = approval1_instance.to_dict()
# create an instance of Approval1 from a dict
approval1_from_dict = Approval1.from_dict(approval1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


