# Event

Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**synced** | **datetime** | A date-time in ISO-8601 format | [optional] 
**action** | **str** | The action that was performed | [optional] 
**type** | **str** | The type of event | [optional] 
**actor** | [**NameType**](NameType.md) |  | [optional] 
**target** | [**NameType**](NameType.md) |  | [optional] 
**stack** | **str** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**objects** | **List[str]** |  | [optional] 
**operation** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 

## Example

```python
from sailpoint.v3.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


