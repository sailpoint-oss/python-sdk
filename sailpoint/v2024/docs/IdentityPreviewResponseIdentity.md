# IdentityPreviewResponseIdentity

Identity's basic details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identity&#39;s DTO type. | [optional] 
**id** | **str** | Identity ID. | [optional] 
**name** | **str** | Identity&#39;s display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_preview_response_identity import IdentityPreviewResponseIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityPreviewResponseIdentity from a JSON string
identity_preview_response_identity_instance = IdentityPreviewResponseIdentity.from_json(json)
# print the JSON string representation of the object
print(IdentityPreviewResponseIdentity.to_json())

# convert the object into a dict
identity_preview_response_identity_dict = identity_preview_response_identity_instance.to_dict()
# create an instance of IdentityPreviewResponseIdentity from a dict
identity_preview_response_identity_from_dict = IdentityPreviewResponseIdentity.from_dict(identity_preview_response_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


