# IdentityAttributePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the attribute that is being previewed. | [optional] 
**value** | **str** | Value that was derived during the preview. | [optional] 
**previous_value** | **str** | The value of the attribute before the preview. | [optional] 
**error_messages** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.identity_attribute_preview import IdentityAttributePreview

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributePreview from a JSON string
identity_attribute_preview_instance = IdentityAttributePreview.from_json(json)
# print the JSON string representation of the object
print(IdentityAttributePreview.to_json())

# convert the object into a dict
identity_attribute_preview_dict = identity_attribute_preview_instance.to_dict()
# create an instance of IdentityAttributePreview from a dict
identity_attribute_preview_from_dict = IdentityAttributePreview.from_dict(identity_attribute_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


