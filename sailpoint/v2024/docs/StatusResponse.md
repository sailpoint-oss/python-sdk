# StatusResponse

Response model for connection check, configuration test and ping of source connectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the source | [optional] [readonly] 
**name** | **str** | Name of the source | [optional] [readonly] 
**status** | **str** | The status of the health check. | [optional] [readonly] 
**elapsed_millis** | **int** | The number of milliseconds spent on the entire request. | [optional] [readonly] 
**details** | **object** | The document contains the results of the health check. The schema of this document depends on the type of source used.  | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.status_response import StatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponse from a JSON string
status_response_instance = StatusResponse.from_json(json)
# print the JSON string representation of the object
print(StatusResponse.to_json())

# convert the object into a dict
status_response_dict = status_response_instance.to_dict()
# create an instance of StatusResponse from a dict
status_response_from_dict = StatusResponse.from_dict(status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


