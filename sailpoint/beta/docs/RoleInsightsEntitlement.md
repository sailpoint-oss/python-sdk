# RoleInsightsEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the entitlement | [optional] 
**id** | **str** | Id of the entitlement | [optional] 
**description** | **str** | Description for the entitlement | [optional] 
**source** | **str** | Source or the application for the entitlement | [optional] 
**attribute** | **str** | Attribute for the entitlement | [optional] 
**value** | **str** | Attribute value for the entitlement | [optional] 

## Example

```python
from sailpoint.beta.models.role_insights_entitlement import RoleInsightsEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsEntitlement from a JSON string
role_insights_entitlement_instance = RoleInsightsEntitlement.from_json(json)
# print the JSON string representation of the object
print(RoleInsightsEntitlement.to_json())

# convert the object into a dict
role_insights_entitlement_dict = role_insights_entitlement_instance.to_dict()
# create an instance of RoleInsightsEntitlement from a dict
role_insights_entitlement_from_dict = RoleInsightsEntitlement.from_dict(role_insights_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


