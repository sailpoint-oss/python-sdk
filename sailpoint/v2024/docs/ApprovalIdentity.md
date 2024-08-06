# ApprovalIdentity

Identity Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID | [optional] 
**type** | **str** | Indication of what group the identity belongs to. Ie, IDENTITY, GOVERNANCE_GROUP, etc | [optional] 
**name** | **str** | Name of the identity | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_identity import ApprovalIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalIdentity from a JSON string
approval_identity_instance = ApprovalIdentity.from_json(json)
# print the JSON string representation of the object
print ApprovalIdentity.to_json()

# convert the object into a dict
approval_identity_dict = approval_identity_instance.to_dict()
# create an instance of ApprovalIdentity from a dict
approval_identity_form_dict = approval_identity.from_dict(approval_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


