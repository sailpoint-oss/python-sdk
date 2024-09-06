# Schedule1Days


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**SelectorAccountMatchConfig**](SelectorAccountMatchConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule1_days import Schedule1Days

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1Days from a JSON string
schedule1_days_instance = Schedule1Days.from_json(json)
# print the JSON string representation of the object
print(Schedule1Days.to_json())

# convert the object into a dict
schedule1_days_dict = schedule1_days_instance.to_dict()
# create an instance of Schedule1Days from a dict
schedule1_days_from_dict = Schedule1Days.from_dict(schedule1_days_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


