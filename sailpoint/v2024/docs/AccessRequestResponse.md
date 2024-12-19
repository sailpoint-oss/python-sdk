# AccessRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_requests** | [**List[AccessRequestTracking]**](AccessRequestTracking.md) | A list of new access request tracking data mapped to the values requested. | [optional] 
**existing_requests** | [**List[AccessRequestTracking]**](AccessRequestTracking.md) | A list of existing access request tracking data mapped to the values requested.  This indicates access has already been requested for this item. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_response import AccessRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestResponse from a JSON string
access_request_response_instance = AccessRequestResponse.from_json(json)
# print the JSON string representation of the object
print(AccessRequestResponse.to_json())

# convert the object into a dict
access_request_response_dict = access_request_response_instance.to_dict()
# create an instance of AccessRequestResponse from a dict
access_request_response_from_dict = AccessRequestResponse.from_dict(access_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


