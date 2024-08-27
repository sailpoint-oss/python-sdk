# ValidateFilterOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | When this field is true, the filter expression is valid against the input. | [optional] [default to False]
**is_valid_json_path** | **bool** | When this field is true, the filter expression is using a valid JSON path. | [optional] [default to False]
**is_path_exist** | **bool** | When this field is true, the filter expression is using an existing path. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.validate_filter_output_dto import ValidateFilterOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateFilterOutputDto from a JSON string
validate_filter_output_dto_instance = ValidateFilterOutputDto.from_json(json)
# print the JSON string representation of the object
print(ValidateFilterOutputDto.to_json())

# convert the object into a dict
validate_filter_output_dto_dict = validate_filter_output_dto_instance.to_dict()
# create an instance of ValidateFilterOutputDto from a dict
validate_filter_output_dto_from_dict = ValidateFilterOutputDto.from_dict(validate_filter_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


