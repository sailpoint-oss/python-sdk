# UpdateMultiHostSourcesRequest

A JSONPatch document as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902).  Only `replace` operations are accepted by this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | Operations to be applied. | [optional] 

## Example

```python
from sailpoint.beta.models.update_multi_host_sources_request import UpdateMultiHostSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMultiHostSourcesRequest from a JSON string
update_multi_host_sources_request_instance = UpdateMultiHostSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMultiHostSourcesRequest.to_json())

# convert the object into a dict
update_multi_host_sources_request_dict = update_multi_host_sources_request_instance.to_dict()
# create an instance of UpdateMultiHostSourcesRequest from a dict
update_multi_host_sources_request_from_dict = UpdateMultiHostSourcesRequest.from_dict(update_multi_host_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


