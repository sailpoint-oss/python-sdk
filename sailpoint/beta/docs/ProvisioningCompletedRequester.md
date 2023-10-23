# ProvisioningCompletedRequester

Reference to the identity (if any) who submitted the provisioning request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.provisioning_completed_requester import ProvisioningCompletedRequester

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedRequester from a JSON string
provisioning_completed_requester_instance = ProvisioningCompletedRequester.from_json(json)
# print the JSON string representation of the object
print ProvisioningCompletedRequester.to_json()

# convert the object into a dict
provisioning_completed_requester_dict = provisioning_completed_requester_instance.to_dict()
# create an instance of ProvisioningCompletedRequester from a dict
provisioning_completed_requester_form_dict = provisioning_completed_requester.from_dict(provisioning_completed_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


