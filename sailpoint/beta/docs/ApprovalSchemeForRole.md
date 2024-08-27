# ApprovalSchemeForRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approver_type** | **str** | Describes the individual or group that is responsible for an approval step. Values are as follows.  **OWNER**: Owner of the associated Role  **MANAGER**: Manager of the Identity making the request  **GOVERNANCE_GROUP**: A Governance Group, the ID of which is specified by the **approverId** field | [optional] 
**approver_id** | **str** | Id of the specific approver, used only when approverType is GOVERNANCE_GROUP | [optional] 

## Example

```python
from sailpoint.beta.models.approval_scheme_for_role import ApprovalSchemeForRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalSchemeForRole from a JSON string
approval_scheme_for_role_instance = ApprovalSchemeForRole.from_json(json)
# print the JSON string representation of the object
print(ApprovalSchemeForRole.to_json())

# convert the object into a dict
approval_scheme_for_role_dict = approval_scheme_for_role_instance.to_dict()
# create an instance of ApprovalSchemeForRole from a dict
approval_scheme_for_role_from_dict = ApprovalSchemeForRole.from_dict(approval_scheme_for_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


