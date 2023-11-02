# IdentityPreviewResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityPreviewResponseIdentity**](IdentityPreviewResponseIdentity.md) |  | [optional] 
**preview_attributes** | [**List[IdentityAttributePreview]**](IdentityAttributePreview.md) |  | [optional] 

## Example

```python
from beta.models.identity_preview_response import IdentityPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityPreviewResponse from a JSON string
identity_preview_response_instance = IdentityPreviewResponse.from_json(json)
# print the JSON string representation of the object
print IdentityPreviewResponse.to_json()

# convert the object into a dict
identity_preview_response_dict = identity_preview_response_instance.to_dict()
# create an instance of IdentityPreviewResponse from a dict
identity_preview_response_form_dict = identity_preview_response.from_dict(identity_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


