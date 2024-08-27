# RevocabilityForRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments_required** | **bool** | Whether the requester of the containing object must provide comments justifying the request | [optional] [default to False]
**denial_comments_required** | **bool** | Whether an approver must provide comments when denying the request | [optional] [default to False]
**approval_schemes** | [**List[ApprovalSchemeForRole]**](ApprovalSchemeForRole.md) | List describing the steps in approving the revocation request | [optional] 

## Example

```python
from sailpoint.v3.models.revocability_for_role import RevocabilityForRole

# TODO update the JSON string below
json = "{}"
# create an instance of RevocabilityForRole from a JSON string
revocability_for_role_instance = RevocabilityForRole.from_json(json)
# print the JSON string representation of the object
print(RevocabilityForRole.to_json())

# convert the object into a dict
revocability_for_role_dict = revocability_for_role_instance.to_dict()
# create an instance of RevocabilityForRole from a dict
revocability_for_role_from_dict = RevocabilityForRole.from_dict(revocability_for_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


