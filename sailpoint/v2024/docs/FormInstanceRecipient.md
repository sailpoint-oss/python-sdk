# FormInstanceRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier | [optional] 
**type** | **str** | Type is a FormInstanceRecipientType value IDENTITY FormInstanceRecipientIdentity | [optional] 

## Example

```python
from sailpoint.v2024.models.form_instance_recipient import FormInstanceRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of FormInstanceRecipient from a JSON string
form_instance_recipient_instance = FormInstanceRecipient.from_json(json)
# print the JSON string representation of the object
print FormInstanceRecipient.to_json()

# convert the object into a dict
form_instance_recipient_dict = form_instance_recipient_instance.to_dict()
# create an instance of FormInstanceRecipient from a dict
form_instance_recipient_form_dict = form_instance_recipient.from_dict(form_instance_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


