# ProvisioningCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | The reference number of the provisioning request. Useful for tracking status in the Account Activity search interface. | 
**sources** | **str** | One or more sources that the provisioning transaction(s) were done against.  Sources are comma separated. | 
**action** | **str** | Origin of where the provisioning request came from. | [optional] 
**errors** | **List[str]** | A list of any accumulated error messages that occurred during provisioning. | [optional] 
**warnings** | **List[str]** | A list of any accumulated warning messages that occurred during provisioning. | [optional] 
**recipient** | [**ProvisioningCompletedRecipient**](ProvisioningCompletedRecipient.md) |  | 
**requester** | [**ProvisioningCompletedRequester**](ProvisioningCompletedRequester.md) |  | [optional] 
**account_requests** | [**List[ProvisioningCompletedAccountRequestsInner]**](ProvisioningCompletedAccountRequestsInner.md) | A list of provisioning instructions to perform on an account-by-account basis. | 

## Example

```python
from sailpoint.beta.models.provisioning_completed import ProvisioningCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompleted from a JSON string
provisioning_completed_instance = ProvisioningCompleted.from_json(json)
# print the JSON string representation of the object
print ProvisioningCompleted.to_json()

# convert the object into a dict
provisioning_completed_dict = provisioning_completed_instance.to_dict()
# create an instance of ProvisioningCompleted from a dict
provisioning_completed_form_dict = provisioning_completed.from_dict(provisioning_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


