# SodRecipient

SOD policy recipient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SOD policy recipient DTO type. | [optional] 
**id** | **str** | SOD policy recipient&#39;s identity ID. | [optional] 
**name** | **str** | SOD policy recipient&#39;s display name. | [optional] 

## Example

```python
from sailpoint.beta.models.sod_recipient import SodRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of SodRecipient from a JSON string
sod_recipient_instance = SodRecipient.from_json(json)
# print the JSON string representation of the object
print SodRecipient.to_json()

# convert the object into a dict
sod_recipient_dict = sod_recipient_instance.to_dict()
# create an instance of SodRecipient from a dict
sod_recipient_form_dict = sod_recipient.from_dict(sod_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


