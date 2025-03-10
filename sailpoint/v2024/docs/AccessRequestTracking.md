# AccessRequestTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_for** | **str** | The identity id in which the access request is for. | [optional] 
**requested_items_details** | [**List[RequestedItemDetails]**](RequestedItemDetails.md) | The details of the item requested. | [optional] 
**attributes_hash** | **int** | a hash representation of the access requested, useful for longer term tracking client side. | [optional] 
**access_request_ids** | **List[str]** | a list of access request identifiers, generally only one will be populated, but high volume requested may result in multiple ids. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_tracking import AccessRequestTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestTracking from a JSON string
access_request_tracking_instance = AccessRequestTracking.from_json(json)
# print the JSON string representation of the object
print(AccessRequestTracking.to_json())

# convert the object into a dict
access_request_tracking_dict = access_request_tracking_instance.to_dict()
# create an instance of AccessRequestTracking from a dict
access_request_tracking_from_dict = AccessRequestTracking.from_dict(access_request_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


