# JsonPatch

A JSONPatch document as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | Operations to be applied | [optional] 

## Example

```python
from sailpoint.v2024.models.json_patch import JsonPatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatch from a JSON string
json_patch_instance = JsonPatch.from_json(json)
# print the JSON string representation of the object
print(JsonPatch.to_json())

# convert the object into a dict
json_patch_dict = json_patch_instance.to_dict()
# create an instance of JsonPatch from a dict
json_patch_from_dict = JsonPatch.from_dict(json_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


