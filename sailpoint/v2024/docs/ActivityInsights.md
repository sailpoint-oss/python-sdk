# ActivityInsights

Insights into account activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | UUID of the account | [optional] 
**usage_days** | **int** | The number of days of activity | [optional] 
**usage_days_state** | **str** | Status indicating if the activity is complete or unknown | [optional] 

## Example

```python
from sailpoint.v2024.models.activity_insights import ActivityInsights

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityInsights from a JSON string
activity_insights_instance = ActivityInsights.from_json(json)
# print the JSON string representation of the object
print(ActivityInsights.to_json())

# convert the object into a dict
activity_insights_dict = activity_insights_instance.to_dict()
# create an instance of ActivityInsights from a dict
activity_insights_from_dict = ActivityInsights.from_dict(activity_insights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


