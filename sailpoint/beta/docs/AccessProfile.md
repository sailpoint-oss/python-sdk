# AccessProfile

Access Profile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Access Profile | [optional] [readonly] 
**name** | **str** | Name of the Access Profile | 
**description** | **str** | Information about the Access Profile | [optional] 
**created** | **datetime** | Date the Access Profile was created | [optional] [readonly] 
**modified** | **datetime** | Date the Access Profile was last modified. | [optional] [readonly] 
**enabled** | **bool** | Whether the Access Profile is enabled. If the Access Profile is enabled then you must include at least one Entitlement. | [optional] [default to True]
**owner** | [**OwnerReference**](OwnerReference.md) |  | 
**source** | [**AccessProfileSourceRef**](AccessProfileSourceRef.md) |  | 
**entitlements** | [**List[EntitlementRef]**](EntitlementRef.md) | A list of entitlements associated with the Access Profile. If enabled is false this is allowed to be empty otherwise it needs to contain at least one Entitlement. | [optional] 
**requestable** | **bool** | Whether the Access Profile is requestable via access request. Currently, making an Access Profile non-requestable is only supported  for customers enabled with the new Request Center. Otherwise, attempting to create an Access Profile with a value  **false** in this field results in a 400 error. | [optional] [default to True]
**access_request_config** | [**Requestability**](Requestability.md) |  | [optional] 
**revocation_request_config** | [**Revocability**](Revocability.md) |  | [optional] 
**segments** | **List[str]** | List of IDs of segments, if any, to which this Access Profile is assigned. | [optional] 
**provisioning_criteria** | [**ProvisioningCriteriaLevel1**](ProvisioningCriteriaLevel1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.access_profile import AccessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfile from a JSON string
access_profile_instance = AccessProfile.from_json(json)
# print the JSON string representation of the object
print AccessProfile.to_json()

# convert the object into a dict
access_profile_dict = access_profile_instance.to_dict()
# create an instance of AccessProfile from a dict
access_profile_form_dict = access_profile.from_dict(access_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


