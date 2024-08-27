# RoleInsightsInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The number of identities in this role with the entitlement. | [optional] 
**identities_with_access** | **int** | The number of identities in this role with the entitlement. | [optional] 
**identities_impacted** | **int** | The number of identities in this role that do not have the specified entitlement. | [optional] 
**total_number_of_identities** | **int** | The total number of identities. | [optional] 
**impacted_identity_names** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_insights_insight import RoleInsightsInsight

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsInsight from a JSON string
role_insights_insight_instance = RoleInsightsInsight.from_json(json)
# print the JSON string representation of the object
print(RoleInsightsInsight.to_json())

# convert the object into a dict
role_insights_insight_dict = role_insights_insight_instance.to_dict()
# create an instance of RoleInsightsInsight from a dict
role_insights_insight_from_dict = RoleInsightsInsight.from_dict(role_insights_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


