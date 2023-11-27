# ScheduleHours

Specifies which hour(s) a schedule is active for. Examples:  Every three hours starting from 8AM, inclusive: * type LIST * values \"8\" * interval 3  During business hours: * type RANGE * values \"9\", \"5\"  At 5AM, noon, and 5PM: * type LIST * values \"5\", \"12\", \"17\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Enum type to specify hours value | 
**values** | **List[str]** | Values of the days based on the enum type mentioned above | 
**interval** | **int** | Interval between the cert generations | [optional] 

## Example

```python
from sailpoint.v3.models.schedule_hours import ScheduleHours

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleHours from a JSON string
schedule_hours_instance = ScheduleHours.from_json(json)
# print the JSON string representation of the object
print ScheduleHours.to_json()

# convert the object into a dict
schedule_hours_dict = schedule_hours_instance.to_dict()
# create an instance of ScheduleHours from a dict
schedule_hours_form_dict = schedule_hours.from_dict(schedule_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


