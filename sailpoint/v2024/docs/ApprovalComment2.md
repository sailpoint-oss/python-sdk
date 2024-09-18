# ApprovalComment2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The comment text | [optional] 
**commenter** | **str** | The name of the commenter | [optional] 
**var_date** | **datetime** | A date-time in ISO-8601 format | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_comment2 import ApprovalComment2

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalComment2 from a JSON string
approval_comment2_instance = ApprovalComment2.from_json(json)
# print the JSON string representation of the object
print(ApprovalComment2.to_json())

# convert the object into a dict
approval_comment2_dict = approval_comment2_instance.to_dict()
# create an instance of ApprovalComment2 from a dict
approval_comment2_from_dict = ApprovalComment2.from_dict(approval_comment2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


