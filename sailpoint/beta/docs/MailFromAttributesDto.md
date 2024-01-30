# MailFromAttributesDto

MAIL FROM attributes for a domain / identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | **str** | The identity or domain address | [optional] 
**mail_from_domain** | **str** | The new MAIL FROM domain of the identity. Must be a subdomain of the identity. | [optional] 

## Example

```python
from sailpoint.beta.models.mail_from_attributes_dto import MailFromAttributesDto

# TODO update the JSON string below
json = "{}"
# create an instance of MailFromAttributesDto from a JSON string
mail_from_attributes_dto_instance = MailFromAttributesDto.from_json(json)
# print the JSON string representation of the object
print MailFromAttributesDto.to_json()

# convert the object into a dict
mail_from_attributes_dto_dict = mail_from_attributes_dto_instance.to_dict()
# create an instance of MailFromAttributesDto from a dict
mail_from_attributes_dto_form_dict = mail_from_attributes_dto.from_dict(mail_from_attributes_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


