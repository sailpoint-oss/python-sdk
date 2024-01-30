# ProvisioningCompletedRecipient

Provisioning recpient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provisioning recipient DTO type. | 
**id** | **str** | Provisioning recipient&#39;s identity ID. | 
**name** | **str** | Provisioning recipient&#39;s display name. | 

## Example

```python
from sailpoint.beta.models.provisioning_completed_recipient import ProvisioningCompletedRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedRecipient from a JSON string
provisioning_completed_recipient_instance = ProvisioningCompletedRecipient.from_json(json)
# print the JSON string representation of the object
print ProvisioningCompletedRecipient.to_json()

# convert the object into a dict
provisioning_completed_recipient_dict = provisioning_completed_recipient_instance.to_dict()
# create an instance of ProvisioningCompletedRecipient from a dict
provisioning_completed_recipient_form_dict = provisioning_completed_recipient.from_dict(provisioning_completed_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


