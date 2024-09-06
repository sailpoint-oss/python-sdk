# Schedule1Hours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The application id | [optional] 
**account_match_config** | [**SelectorAccountMatchConfig**](SelectorAccountMatchConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule1_hours import Schedule1Hours

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1Hours from a JSON string
schedule1_hours_instance = Schedule1Hours.from_json(json)
# print the JSON string representation of the object
print(Schedule1Hours.to_json())

# convert the object into a dict
schedule1_hours_dict = schedule1_hours_instance.to_dict()
# create an instance of Schedule1Hours from a dict
schedule1_hours_from_dict = Schedule1Hours.from_dict(schedule1_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


