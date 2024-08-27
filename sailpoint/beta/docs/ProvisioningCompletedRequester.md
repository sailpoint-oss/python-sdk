# ProvisioningCompletedRequester

Provisioning requester's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provisioning requester&#39;s DTO type. | 
**id** | **str** | Provisioning requester&#39;s identity ID. | 
**name** | **str** | Provisioning owner&#39;s human-readable display name. | 

## Example

```python
from sailpoint.beta.models.provisioning_completed_requester import ProvisioningCompletedRequester

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedRequester from a JSON string
provisioning_completed_requester_instance = ProvisioningCompletedRequester.from_json(json)
# print the JSON string representation of the object
print(ProvisioningCompletedRequester.to_json())

# convert the object into a dict
provisioning_completed_requester_dict = provisioning_completed_requester_instance.to_dict()
# create an instance of ProvisioningCompletedRequester from a dict
provisioning_completed_requester_from_dict = ProvisioningCompletedRequester.from_dict(provisioning_completed_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


