# UpdateMultiHostSourcesRequestInner

A JSONPatch Operation as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation to be performed | 
**path** | **str** | A string JSON Pointer representing the target path to an element to be affected by the operation | 
**value** | [**UpdateMultiHostSourcesRequestInnerValue**](UpdateMultiHostSourcesRequestInnerValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.update_multi_host_sources_request_inner import UpdateMultiHostSourcesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMultiHostSourcesRequestInner from a JSON string
update_multi_host_sources_request_inner_instance = UpdateMultiHostSourcesRequestInner.from_json(json)
# print the JSON string representation of the object
print(UpdateMultiHostSourcesRequestInner.to_json())

# convert the object into a dict
update_multi_host_sources_request_inner_dict = update_multi_host_sources_request_inner_instance.to_dict()
# create an instance of UpdateMultiHostSourcesRequestInner from a dict
update_multi_host_sources_request_inner_from_dict = UpdateMultiHostSourcesRequestInner.from_dict(update_multi_host_sources_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


