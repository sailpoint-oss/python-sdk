# EntitlementApprovalScheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approver_type** | **str** | Describes the individual or group that is responsible for an approval step. Values are as follows.  **ENTITLEMENT_OWNER**: Owner of the associated Entitlement  **SOURCE_OWNER**: Owner of the associated Source  **MANAGER**: Manager of the Identity for whom the request is being made  **GOVERNANCE_GROUP**: A Governance Group, the ID of which is specified by the **approverId** field | [optional] 
**approver_id** | **str** | Id of the specific approver, used only when approverType is GOVERNANCE_GROUP | [optional] 

## Example

```python
from sailpoint.beta.models.entitlement_approval_scheme import EntitlementApprovalScheme

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementApprovalScheme from a JSON string
entitlement_approval_scheme_instance = EntitlementApprovalScheme.from_json(json)
# print the JSON string representation of the object
print EntitlementApprovalScheme.to_json()

# convert the object into a dict
entitlement_approval_scheme_dict = entitlement_approval_scheme_instance.to_dict()
# create an instance of EntitlementApprovalScheme from a dict
entitlement_approval_scheme_form_dict = entitlement_approval_scheme.from_dict(entitlement_approval_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


