# ValidateFilterInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **object** | Mock input to evaluate filter expression against. | 
**filter** | **str** | JSONPath filter to conditionally invoke trigger when expression evaluates to true. | 

## Example

```python
from sailpoint.beta.models.validate_filter_input_dto import ValidateFilterInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateFilterInputDto from a JSON string
validate_filter_input_dto_instance = ValidateFilterInputDto.from_json(json)
# print the JSON string representation of the object
print ValidateFilterInputDto.to_json()

# convert the object into a dict
validate_filter_input_dto_dict = validate_filter_input_dto_instance.to_dict()
# create an instance of ValidateFilterInputDto from a dict
validate_filter_input_dto_form_dict = validate_filter_input_dto.from_dict(validate_filter_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


