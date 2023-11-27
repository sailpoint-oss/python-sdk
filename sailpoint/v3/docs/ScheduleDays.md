# ScheduleDays

Specifies which day(s) a schedule is active for. This is required for all schedule types. The \"values\" field holds different data depending on the type of schedule: * WEEKLY: days of the week (1-7) * MONTHLY: days of the month (1-31, L, L-1...) * ANNUALLY: if the \"months\" field is also set: days of the month (1-31, L, L-1...); otherwise: ISO-8601 dates without year (\"--12-31\") * CALENDAR: ISO-8601 dates (\"2020-12-31\")  Note that CALENDAR only supports the LIST type, and ANNUALLY does not support the RANGE type when provided with ISO-8601 dates without year.  Examples:  On Sundays: * type LIST * values \"1\"  The second to last day of the month: * type LIST * values \"L-1\"  From the 20th to the last day of the month: * type RANGE * values \"20\", \"L\"  Every March 2nd: * type LIST * values \"--03-02\"  On March 2nd, 2021: * type: LIST * values \"2021-03-02\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Enum type to specify days value | 
**values** | **List[str]** | Values of the days based on the enum type mentioned above | 
**interval** | **int** | Interval between the cert generations | [optional] 

## Example

```python
from sailpoint.v3.models.schedule_days import ScheduleDays

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDays from a JSON string
schedule_days_instance = ScheduleDays.from_json(json)
# print the JSON string representation of the object
print ScheduleDays.to_json()

# convert the object into a dict
schedule_days_dict = schedule_days_instance.to_dict()
# create an instance of ScheduleDays from a dict
schedule_days_form_dict = schedule_days.from_dict(schedule_days_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


