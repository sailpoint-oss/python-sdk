# RoleInsight


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Insight id | [optional] 
**number_of_updates** | **int** | Total number of updates for this role | [optional] 
**created_date** | **datetime** | The date-time insights were last created for this role. | [optional] 
**role** | [**RoleInsightsRole**](RoleInsightsRole.md) |  | [optional] 
**insight** | [**RoleInsightsInsight**](RoleInsightsInsight.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.role_insight import RoleInsight

# TODO update the JSON string below
json = "{}"
# create an instance of RoleInsight from a JSON string
role_insight_instance = RoleInsight.from_json(json)
# print the JSON string representation of the object
print RoleInsight.to_json()

# convert the object into a dict
role_insight_dict = role_insight_instance.to_dict()
# create an instance of RoleInsight from a dict
role_insight_form_dict = role_insight.from_dict(role_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


