# Schedule1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the Schedule. | 
**cron_expression** | **str** | The cron expression of the schedule. | 

## Example

```python
from sailpoint.v2024.models.schedule1 import Schedule1

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule1 from a JSON string
schedule1_instance = Schedule1.from_json(json)
# print the JSON string representation of the object
print(Schedule1.to_json())

# convert the object into a dict
schedule1_dict = schedule1_instance.to_dict()
# create an instance of Schedule1 from a dict
schedule1_from_dict = Schedule1.from_dict(schedule1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


