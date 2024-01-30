# ErrorResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** | **str** | Fine-grained error code providing more detail of the error. | [optional] 
**tracking_id** | **str** | Unique tracking id for the error. | [optional] 
**messages** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) | Generic localized reason for error | [optional] 
**causes** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) | Plain-text descriptive reasons to provide additional detail to the text provided in the messages field | [optional] 

## Example

```python
from sailpoint.v3.models.error_response_dto import ErrorResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseDto from a JSON string
error_response_dto_instance = ErrorResponseDto.from_json(json)
# print the JSON string representation of the object
print ErrorResponseDto.to_json()

# convert the object into a dict
error_response_dto_dict = error_response_dto_instance.to_dict()
# create an instance of ErrorResponseDto from a dict
error_response_dto_form_dict = error_response_dto.from_dict(error_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


