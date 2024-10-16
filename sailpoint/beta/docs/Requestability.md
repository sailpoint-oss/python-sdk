# Requestability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Whether the requester of the containing object must provide comments justifying the request | [optional] [default to False]
**denial_comments_required** | **bool** | Whether an approver must provide comments when denying the request | [optional] [default to False]
**approval_schemes** | [**List[AccessProfileApprovalScheme]**](AccessProfileApprovalScheme.md) | List describing the steps in approving the request | [optional] 

## Example

```python
from sailpoint.beta.models.requestability import Requestability

# TODO update the JSON string below
json = "{}"
# create an instance of Requestability from a JSON string
requestability_instance = Requestability.from_json(json)
# print the JSON string representation of the object
print(Requestability.to_json())

# convert the object into a dict
requestability_dict = requestability_instance.to_dict()
# create an instance of Requestability from a dict
requestability_from_dict = Requestability.from_dict(requestability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


