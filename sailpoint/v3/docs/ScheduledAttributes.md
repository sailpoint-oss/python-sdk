# ScheduledAttributes

Attributes related to a scheduled trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_string** | **str** | A valid CRON expression | 

## Example

```python
from sailpoint.v3.models.scheduled_attributes import ScheduledAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledAttributes from a JSON string
scheduled_attributes_instance = ScheduledAttributes.from_json(json)
# print the JSON string representation of the object
print ScheduledAttributes.to_json()

# convert the object into a dict
scheduled_attributes_dict = scheduled_attributes_instance.to_dict()
# create an instance of ScheduledAttributes from a dict
scheduled_attributes_form_dict = scheduled_attributes.from_dict(scheduled_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


