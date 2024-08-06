# ScheduleMonths

Specifies which months of a schedule are active. Only valid for ANNUALLY schedule types. Examples:  On February and March: * type LIST * values \"2\", \"3\"  Every 3 months, starting in January (quarterly): * type LIST * values \"1\" * interval 3  Every two months between July and December: * type RANGE * values \"7\", \"12\" * interval 2 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Enum type to specify months value | 
**values** | **List[str]** | Values of the months based on the enum type mentioned above | 
**interval** | **int** | Interval between the cert generations | [optional] 

## Example

```python
from sailpoint.v2024.models.schedule_months import ScheduleMonths

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleMonths from a JSON string
schedule_months_instance = ScheduleMonths.from_json(json)
# print the JSON string representation of the object
print ScheduleMonths.to_json()

# convert the object into a dict
schedule_months_dict = schedule_months_instance.to_dict()
# create an instance of ScheduleMonths from a dict
schedule_months_form_dict = schedule_months.from_dict(schedule_months_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


