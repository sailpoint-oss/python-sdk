# ProvisioningCompletedAccountRequestsInnerSource

Reference to the source being provisioned against.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the object to which this reference applies | 
**type** | **str** | The type of object that is referenced | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.provisioning_completed_account_requests_inner_source import ProvisioningCompletedAccountRequestsInnerSource

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedAccountRequestsInnerSource from a JSON string
provisioning_completed_account_requests_inner_source_instance = ProvisioningCompletedAccountRequestsInnerSource.from_json(json)
# print the JSON string representation of the object
print ProvisioningCompletedAccountRequestsInnerSource.to_json()

# convert the object into a dict
provisioning_completed_account_requests_inner_source_dict = provisioning_completed_account_requests_inner_source_instance.to_dict()
# create an instance of ProvisioningCompletedAccountRequestsInnerSource from a dict
provisioning_completed_account_requests_inner_source_form_dict = provisioning_completed_account_requests_inner_source.from_dict(provisioning_completed_account_requests_inner_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


