# ProvisioningCompletedRecipient

Reference to the identity who is the target of the provisioning request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.provisioning_completed_recipient import ProvisioningCompletedRecipient

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


