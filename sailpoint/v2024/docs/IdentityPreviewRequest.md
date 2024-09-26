# IdentityPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The Identity id | [optional] 
**identity_attribute_config** | [**IdentityAttributeConfig**](IdentityAttributeConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_preview_request import IdentityPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityPreviewRequest from a JSON string
identity_preview_request_instance = IdentityPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(IdentityPreviewRequest.to_json())

# convert the object into a dict
identity_preview_request_dict = identity_preview_request_instance.to_dict()
# create an instance of IdentityPreviewRequest from a dict
identity_preview_request_from_dict = IdentityPreviewRequest.from_dict(identity_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


