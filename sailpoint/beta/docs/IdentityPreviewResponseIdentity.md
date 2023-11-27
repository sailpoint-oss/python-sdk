# IdentityPreviewResponseIdentity

Identity's manager.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity&#39;s manager. | [optional] 
**id** | **str** | ID of identity&#39;s manager. | [optional] 
**name** | **str** | Human-readable display name of identity&#39;s manager. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_preview_response_identity import IdentityPreviewResponseIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityPreviewResponseIdentity from a JSON string
identity_preview_response_identity_instance = IdentityPreviewResponseIdentity.from_json(json)
# print the JSON string representation of the object
print IdentityPreviewResponseIdentity.to_json()

# convert the object into a dict
identity_preview_response_identity_dict = identity_preview_response_identity_instance.to_dict()
# create an instance of IdentityPreviewResponseIdentity from a dict
identity_preview_response_identity_form_dict = identity_preview_response_identity.from_dict(identity_preview_response_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


