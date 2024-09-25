# TestSourceConnectionMultihost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Source&#39;s test connection status. | [optional] 
**message** | **str** | Source&#39;s test connection message. | [optional] 
**timing** | **int** | Source&#39;s test connection timing. | [optional] 
**result_type** | **object** | Source&#39;s human-readable result type. | [optional] 
**test_connection_details** | **str** | Source&#39;s human-readable test connection details. | [optional] 

## Example

```python
from sailpoint.beta.models.test_source_connection_multihost200_response import TestSourceConnectionMultihost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TestSourceConnectionMultihost200Response from a JSON string
test_source_connection_multihost200_response_instance = TestSourceConnectionMultihost200Response.from_json(json)
# print the JSON string representation of the object
print(TestSourceConnectionMultihost200Response.to_json())

# convert the object into a dict
test_source_connection_multihost200_response_dict = test_source_connection_multihost200_response_instance.to_dict()
# create an instance of TestSourceConnectionMultihost200Response from a dict
test_source_connection_multihost200_response_from_dict = TestSourceConnectionMultihost200Response.from_dict(test_source_connection_multihost200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


