# MailFromAttributes

MAIL FROM attributes for a domain / identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | **str** | The email identity | [optional] 
**mail_from_domain** | **str** | The name of a domain that an email identity uses as a custom MAIL FROM domain | [optional] 
**mx_record** | **str** | MX record that is required in customer&#39;s DNS to allow the domain to receive bounce and complaint notifications that email providers send you | [optional] 
**txt_record** | **str** | TXT record that is required in customer&#39;s DNS in order to prove that Amazon SES is authorized to send email from your domain | [optional] 
**mail_from_domain_status** | **str** | The current status of the MAIL FROM verification | [optional] 

## Example

```python
from sailpoint.beta.models.mail_from_attributes import MailFromAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MailFromAttributes from a JSON string
mail_from_attributes_instance = MailFromAttributes.from_json(json)
# print the JSON string representation of the object
print(MailFromAttributes.to_json())

# convert the object into a dict
mail_from_attributes_dict = mail_from_attributes_instance.to_dict()
# create an instance of MailFromAttributes from a dict
mail_from_attributes_from_dict = MailFromAttributes.from_dict(mail_from_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


