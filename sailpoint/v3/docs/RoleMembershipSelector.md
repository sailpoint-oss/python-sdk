# RoleMembershipSelector

When present, specifies that the Role is to be granted to Identities which either satisfy specific criteria or which are members of a given list of Identities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoleMembershipSelectorType**](RoleMembershipSelectorType.md) |  | [optional] 
**criteria** | [**RoleCriteriaLevel1**](RoleCriteriaLevel1.md) |  | [optional] 
**identities** | [**List[RoleMembershipIdentity]**](RoleMembershipIdentity.md) | Defines role membership as being exclusive to the specified Identities, when type is IDENTITY_LIST. | [optional] 

## Example

```python
from sailpoint.v3.models.role_membership_selector import RoleMembershipSelector

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMembershipSelector from a JSON string
role_membership_selector_instance = RoleMembershipSelector.from_json(json)
# print the JSON string representation of the object
print RoleMembershipSelector.to_json()

# convert the object into a dict
role_membership_selector_dict = role_membership_selector_instance.to_dict()
# create an instance of RoleMembershipSelector from a dict
role_membership_selector_form_dict = role_membership_selector.from_dict(role_membership_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


