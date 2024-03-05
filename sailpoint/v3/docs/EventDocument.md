# EventDocument

Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**synced** | **str** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**action** | **str** | Name of the event as it&#39;s displayed in audit reports. | [optional] 
**type** | **str** | Event type. Refer to [Event Types](https://documentation.sailpoint.com/saas/help/search/index.html#event-types) for a list of event types and their meanings. | [optional] 
**actor** | **str** | Name of the actor that generated the event. | [optional] 
**target** | **str** | Name of the target, or recipient, of the event. | [optional] 
**stack** | **str** | The event&#39;s stack. | [optional] 
**tracking_number** | **str** | ID of the group of events. | [optional] 
**ip_address** | **str** | Target system&#39;s IP address. | [optional] 
**details** | **str** | ID of event&#39;s details. | [optional] 
**attributes** | **Dict[str, object]** | Attributes involved in the event. | [optional] 
**objects** | **List[str]** | Objects the event is happening to. | [optional] 
**operation** | **str** | Operation, or action, performed during the event. | [optional] 
**status** | **str** | Event status. Refer to [Event Statuses](https://documentation.sailpoint.com/saas/help/search/index.html#event-statuses) for a list of event statuses and their meanings. | [optional] 
**technical_name** | **str** | Event&#39;s normalized name. This normalized name always follows the pattern of &#39;objects_operation_status&#39;. | [optional] 

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


