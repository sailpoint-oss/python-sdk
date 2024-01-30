# EventDocument

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
from sailpoint.v3.models.event_document import EventDocument

# TODO update the JSON string below
json = "{}"
# create an instance of EventDocument from a JSON string
event_document_instance = EventDocument.from_json(json)
# print the JSON string representation of the object
print EventDocument.to_json()

# convert the object into a dict
event_document_dict = event_document_instance.to_dict()
# create an instance of EventDocument from a dict
event_document_form_dict = event_document.from_dict(event_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


