# RequestedItemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of access item requested. | [optional] 
**id** | **str** | The id of the access item requested. | [optional] 

## Example

```python
from sailpoint.v3.models.requested_item_details import RequestedItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemDetails from a JSON string
requested_item_details_instance = RequestedItemDetails.from_json(json)
# print the JSON string representation of the object
print(RequestedItemDetails.to_json())

# convert the object into a dict
requested_item_details_dict = requested_item_details_instance.to_dict()
# create an instance of RequestedItemDetails from a dict
requested_item_details_from_dict = RequestedItemDetails.from_dict(requested_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


