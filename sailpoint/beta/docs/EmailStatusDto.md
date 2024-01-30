# EmailStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.email_status_dto import EmailStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStatusDto from a JSON string
email_status_dto_instance = EmailStatusDto.from_json(json)
# print the JSON string representation of the object
print EmailStatusDto.to_json()

# convert the object into a dict
email_status_dto_dict = email_status_dto_instance.to_dict()
# create an instance of EmailStatusDto from a dict
email_status_dto_form_dict = email_status_dto.from_dict(email_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


