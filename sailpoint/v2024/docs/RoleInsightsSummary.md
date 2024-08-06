# RoleInsightsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_updates** | **int** | Total number of roles with updates | [optional] 
**last_generated** | **datetime** | The date-time role insights were last found. | [optional] 
**entitlements_included_in_roles** | **int** | The number of entitlements included in roles (vs free radicals). | [optional] 
**total_number_of_entitlements** | **int** | The total number of entitlements. | [optional] 
**identities_with_access_via_roles** | **int** | The number of identities in roles vs. identities with just entitlements and not in roles. | [optional] 
**total_number_of_identities** | **int** | The total number of identities. | [optional] 

## Example

```python
from sailpoint.v2024.models.role_insights_summary import RoleInsightsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsightsSummary from a JSON string
role_insights_summary_instance = RoleInsightsSummary.from_json(json)
# print the JSON string representation of the object
print RoleInsightsSummary.to_json()

# convert the object into a dict
role_insights_summary_dict = role_insights_summary_instance.to_dict()
# create an instance of RoleInsightsSummary from a dict
role_insights_summary_form_dict = role_insights_summary.from_dict(role_insights_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


