# Schedule1

The schedule information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScheduleType**](ScheduleType.md) |  | 
**days** | [**Schedule1Days**](Schedule1Days.md) |  | [optional] 
**hours** | [**Schedule1Hours**](Schedule1Hours.md) |  | 
**expiration** | **datetime** | A date-time in ISO-8601 format | [optional] 
**time_zone_id** | **str** | The canonical TZ identifier the schedule will run in (ex. America/New_York).  If no timezone is specified, the org&#39;s default timezone is used. | [optional] 

## Example

```python
from sailpoint.v3.models.schedule1 import Schedule1

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1 from a JSON string
schedule1_instance = Schedule1.from_json(json)
# print the JSON string representation of the object
print Schedule1.to_json()

# convert the object into a dict
schedule1_dict = schedule1_instance.to_dict()
# create an instance of Schedule1 from a dict
schedule1_form_dict = schedule1.from_dict(schedule1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


