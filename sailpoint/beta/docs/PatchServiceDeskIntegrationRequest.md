# PatchServiceDeskIntegrationRequest

A JSONPatch document as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902).  Only `replace` operations are accepted by this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) | Operations to be applied | [optional] 

## Example

```python
from sailpoint.beta.models.patch_service_desk_integration_request import PatchServiceDeskIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServiceDeskIntegrationRequest from a JSON string
patch_service_desk_integration_request_instance = PatchServiceDeskIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServiceDeskIntegrationRequest.to_json())

# convert the object into a dict
patch_service_desk_integration_request_dict = patch_service_desk_integration_request_instance.to_dict()
# create an instance of PatchServiceDeskIntegrationRequest from a dict
patch_service_desk_integration_request_from_dict = PatchServiceDeskIntegrationRequest.from_dict(patch_service_desk_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


