# ApprovalDescription

The description of what the approval is asking for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The description of what the approval is asking for | [optional] 
**locale** | **str** | What locale the description of the approval is using | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_description import ApprovalDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalDescription from a JSON string
approval_description_instance = ApprovalDescription.from_json(json)
# print the JSON string representation of the object
print(ApprovalDescription.to_json())

# convert the object into a dict
approval_description_dict = approval_description_instance.to_dict()
# create an instance of ApprovalDescription from a dict
approval_description_from_dict = ApprovalDescription.from_dict(approval_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


