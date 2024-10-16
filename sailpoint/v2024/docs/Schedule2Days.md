# Schedule2Days


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**SelectorAccountMatchConfig**](SelectorAccountMatchConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule2_days import Schedule2Days

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule2Days from a JSON string
schedule2_days_instance = Schedule2Days.from_json(json)
# print the JSON string representation of the object
print(Schedule2Days.to_json())

# convert the object into a dict
schedule2_days_dict = schedule2_days_instance.to_dict()
# create an instance of Schedule2Days from a dict
schedule2_days_from_dict = Schedule2Days.from_dict(schedule2_days_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


