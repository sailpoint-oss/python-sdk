# Schedule2

The schedule information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScheduleType**](ScheduleType.md) |  | 
**months** | [**Schedule2Months**](Schedule2Months.md) |  | [optional] 
**days** | [**Schedule2Days**](Schedule2Days.md) |  | [optional] 
**hours** | [**Schedule2Hours**](Schedule2Hours.md) |  | 
**expiration** | **datetime** | A date-time in ISO-8601 format | [optional] 
**time_zone_id** | **str** | The canonical TZ identifier the schedule will run in (ex. America/New_York).  If no timezone is specified, the org&#39;s default timezone is used. | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule2 import Schedule2

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule2 from a JSON string
schedule2_instance = Schedule2.from_json(json)
# print the JSON string representation of the object
print(Schedule2.to_json())

# convert the object into a dict
schedule2_dict = schedule2_instance.to_dict()
# create an instance of Schedule2 from a dict
schedule2_from_dict = Schedule2.from_dict(schedule2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


