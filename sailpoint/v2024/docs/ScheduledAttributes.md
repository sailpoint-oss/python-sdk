# ScheduledAttributes

Attributes related to a scheduled trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_string** | **str** | A valid CRON expression | [optional] 
**frequency** | **str** | Frequency of execution | 
**time_zone** | **str** | Time zone identifier | [optional] 
**weekly_days** | **List[str]** | Scheduled days of the week for execution | [optional] 
**weekly_times** | **List[str]** | Scheduled execution times | [optional] 

## Example

```python
from sailpoint.v2024.models.scheduled_attributes import ScheduledAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledAttributes from a JSON string
scheduled_attributes_instance = ScheduledAttributes.from_json(json)
# print the JSON string representation of the object
print(ScheduledAttributes.to_json())

# convert the object into a dict
scheduled_attributes_dict = scheduled_attributes_instance.to_dict()
# create an instance of ScheduledAttributes from a dict
scheduled_attributes_from_dict = ScheduledAttributes.from_dict(scheduled_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


