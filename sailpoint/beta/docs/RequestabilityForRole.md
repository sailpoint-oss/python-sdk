# RequestabilityForRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Whether the requester of the containing object must provide comments justifying the request | [optional] [default to False]
**denial_comments_required** | **bool** | Whether an approver must provide comments when denying the request | [optional] [default to False]
**approval_schemes** | [**List[ApprovalSchemeForRole]**](ApprovalSchemeForRole.md) | List describing the steps in approving the request | [optional] 

## Example

```python
from sailpoint.beta.models.requestability_for_role import RequestabilityForRole

# TODO update the JSON string below
json = "{}"
# create an instance of RequestabilityForRole from a JSON string
requestability_for_role_instance = RequestabilityForRole.from_json(json)
# print the JSON string representation of the object
print RequestabilityForRole.to_json()

# convert the object into a dict
requestability_for_role_dict = requestability_for_role_instance.to_dict()
# create an instance of RequestabilityForRole from a dict
requestability_for_role_form_dict = requestability_for_role.from_dict(requestability_for_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


