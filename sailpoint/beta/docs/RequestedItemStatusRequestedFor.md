# RequestedItemStatusRequestedFor

Identity access was requested for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the object to which this reference applies | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.beta.models.requested_item_status_requested_for import RequestedItemStatusRequestedFor

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusRequestedFor from a JSON string
requested_item_status_requested_for_instance = RequestedItemStatusRequestedFor.from_json(json)
# print the JSON string representation of the object
print RequestedItemStatusRequestedFor.to_json()

# convert the object into a dict
requested_item_status_requested_for_dict = requested_item_status_requested_for_instance.to_dict()
# create an instance of RequestedItemStatusRequestedFor from a dict
requested_item_status_requested_for_form_dict = requested_item_status_requested_for.from_dict(requested_item_status_requested_for_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


