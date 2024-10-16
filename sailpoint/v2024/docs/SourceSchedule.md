# SourceSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the Schedule. | 
**cron_expression** | **str** | The cron expression of the schedule. | 

## Example

```python
from sailpoint.v2024.models.source_schedule import SourceSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SourceSchedule from a JSON string
source_schedule_instance = SourceSchedule.from_json(json)
# print the JSON string representation of the object
print(SourceSchedule.to_json())

# convert the object into a dict
source_schedule_dict = source_schedule_instance.to_dict()
# create an instance of SourceSchedule from a dict
source_schedule_from_dict = SourceSchedule.from_dict(source_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


