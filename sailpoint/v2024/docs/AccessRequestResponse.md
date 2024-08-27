# AccessRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requester_id** | **str** | the requester Id | [optional] 
**requester_name** | **str** | the requesterName | [optional] 
**items** | [**List[AccessRequestItemResponse]**](AccessRequestItemResponse.md) |  | [optional] 

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


