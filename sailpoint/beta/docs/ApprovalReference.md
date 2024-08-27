# ApprovalReference

Reference objects related to the approval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the reference object | [optional] 
**type** | **str** | What reference object does this ID correspond to | [optional] 

## Example

```python
from sailpoint.beta.models.approval_reference import ApprovalReference

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalReference from a JSON string
approval_reference_instance = ApprovalReference.from_json(json)
# print the JSON string representation of the object
print(ApprovalReference.to_json())

# convert the object into a dict
approval_reference_dict = approval_reference_instance.to_dict()
# create an instance of ApprovalReference from a dict
approval_reference_from_dict = ApprovalReference.from_dict(approval_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


