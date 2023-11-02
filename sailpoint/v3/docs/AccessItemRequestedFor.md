# AccessItemRequestedFor

Identity the access item is requested for.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity the access item is requested for. | [optional] 
**id** | **str** | ID of identity the access item is requested for. | [optional] 
**name** | **str** | Human-readable display name of identity the access item is requested for. | [optional] 

## Example

```python
from v3.models.access_item_requested_for import AccessItemRequestedFor

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRequestedFor from a JSON string
access_item_requested_for_instance = AccessItemRequestedFor.from_json(json)
# print the JSON string representation of the object
print AccessItemRequestedFor.to_json()

# convert the object into a dict
access_item_requested_for_dict = access_item_requested_for_instance.to_dict()
# create an instance of AccessItemRequestedFor from a dict
access_item_requested_for_form_dict = access_item_requested_for.from_dict(access_item_requested_for_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


