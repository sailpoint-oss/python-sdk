# TemplateBulkDeleteDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**medium** | **str** |  | [optional] 
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | [optional] 

## Example

```python
from sailpoint.beta.models.template_bulk_delete_dto import TemplateBulkDeleteDto

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateBulkDeleteDto from a JSON string
template_bulk_delete_dto_instance = TemplateBulkDeleteDto.from_json(json)
# print the JSON string representation of the object
print TemplateBulkDeleteDto.to_json()

# convert the object into a dict
template_bulk_delete_dto_dict = template_bulk_delete_dto_instance.to_dict()
# create an instance of TemplateBulkDeleteDto from a dict
template_bulk_delete_dto_form_dict = template_bulk_delete_dto.from_dict(template_bulk_delete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


