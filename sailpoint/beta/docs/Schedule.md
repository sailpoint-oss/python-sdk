# Schedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Determines the overall schedule cadence. In general, all time period fields smaller than the chosen type can be configured. For example, a DAILY schedule can have &#39;hours&#39; set, but not &#39;days&#39;; a WEEKLY schedule can have both &#39;hours&#39; and &#39;days&#39; set. | 
**months** | [**ScheduleMonths**](ScheduleMonths.md) |  | [optional] 
**days** | [**ScheduleDays**](ScheduleDays.md) |  | [optional] 
**hours** | [**ScheduleHours**](ScheduleHours.md) |  | 
**expiration** | **datetime** | Specifies the time after which this schedule will no longer occur. | [optional] 
**time_zone_id** | **str** | The time zone to use when running the schedule. For instance, if the schedule is scheduled to run at 1AM, and this field is set to \&quot;CST\&quot;, the schedule will run at 1AM CST. | [optional] 

## Example

```python
from beta.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print Schedule.to_json()

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_form_dict = schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


