# AccessProfileApprovalScheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approver_type** | **str** | Describes the individual or group that is responsible for an approval step. Values are as follows. **APP_OWNER**: The owner of the Application  **OWNER**: Owner of the associated Access Profile or Role  **SOURCE_OWNER**: Owner of the Source associated with an Access Profile  **MANAGER**: Manager of the Identity making the request  **GOVERNANCE_GROUP**: A Governance Group, the ID of which is specified by the **approverId** field | [optional] 
**approver_id** | **str** | Id of the specific approver, used only when approverType is GOVERNANCE_GROUP | [optional] 

## Example

```python
from sailpoint.v2024.models.access_profile_approval_scheme import AccessProfileApprovalScheme

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileApprovalScheme from a JSON string
access_profile_approval_scheme_instance = AccessProfileApprovalScheme.from_json(json)
# print the JSON string representation of the object
print(AccessProfileApprovalScheme.to_json())

# convert the object into a dict
access_profile_approval_scheme_dict = access_profile_approval_scheme_instance.to_dict()
# create an instance of AccessProfileApprovalScheme from a dict
access_profile_approval_scheme_from_dict = AccessProfileApprovalScheme.from_dict(access_profile_approval_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


