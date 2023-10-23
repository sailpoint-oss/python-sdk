# RoleInsightsEntitlementChanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the entitlement | [optional] 
**id** | **str** | Id of the entitlement | [optional] 
**description** | **str** | Description for the entitlement | [optional] 
**attribute** | **str** | Attribute for the entitlement | [optional] 
**value** | **str** | Attribute value for the entitlement | [optional] 
**source** | **str** | Source or the application for the entitlement | [optional] 
**insight** | [**RoleInsightsInsight**](RoleInsightsInsight.md) |  | [optional] 

## Example

```python
from beta.models.role_insights_entitlement_changes import RoleInsightsEntitlementChanges

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsEntitlementChanges from a JSON string
role_insights_entitlement_changes_instance = RoleInsightsEntitlementChanges.from_json(json)
# print the JSON string representation of the object
print RoleInsightsEntitlementChanges.to_json()

# convert the object into a dict
role_insights_entitlement_changes_dict = role_insights_entitlement_changes_instance.to_dict()
# create an instance of RoleInsightsEntitlementChanges from a dict
role_insights_entitlement_changes_form_dict = role_insights_entitlement_changes.from_dict(role_insights_entitlement_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


