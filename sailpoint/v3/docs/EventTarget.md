# EventTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the target, or recipient, of the event. | [optional] 

## Example

```python
from sailpoint.v3.models.event_target import EventTarget

# TODO update the JSON string below
json = "{}"
# create an instance of EventTarget from a JSON string
event_target_instance = EventTarget.from_json(json)
# print the JSON string representation of the object
print(EventTarget.to_json())

# convert the object into a dict
event_target_dict = event_target_instance.to_dict()
# create an instance of EventTarget from a dict
event_target_from_dict = EventTarget.from_dict(event_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


