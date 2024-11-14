# EventAttributes

Attributes related to an IdentityNow ETS event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the trigger | 
**filter_** | **str** | JSON path expression that will limit which events the trigger will fire on | [optional] 
**description** | **str** | Description of the event trigger | [optional] 

## Example

```python
from sailpoint.beta.models.event_attributes import EventAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttributes from a JSON string
event_attributes_instance = EventAttributes.from_json(json)
# print the JSON string representation of the object
print(EventAttributes.to_json())

# convert the object into a dict
event_attributes_dict = event_attributes_instance.to_dict()
# create an instance of EventAttributes from a dict
event_attributes_from_dict = EventAttributes.from_dict(event_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


