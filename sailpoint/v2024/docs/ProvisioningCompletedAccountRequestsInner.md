# ProvisioningCompletedAccountRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ProvisioningCompletedAccountRequestsInnerSource**](ProvisioningCompletedAccountRequestsInnerSource.md) |  | 
**account_id** | **str** | The unique idenfier of the account being provisioned. | [optional] 
**account_operation** | **str** | The provisioning operation; typically Create, Modify, Enable, Disable, Unlock, or Delete. | 
**provisioning_result** | **object** | The overall result of the provisioning transaction; this could be success, pending, failed, etc. | 
**provisioning_target** | **str** | The name of the provisioning channel selected; this could be the same as the source, or could be a Service Desk Integration Module (SDIM). | 
**ticket_id** | **str** | A reference to a tracking number, if this is sent to a Service Desk Integration Module (SDIM). | [optional] 
**attribute_requests** | [**List[ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner]**](ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner.md) | A list of attributes as part of the provisioning transaction. | [optional] 

## Example

```python
from sailpoint.v2024.models.provisioning_completed_account_requests_inner import ProvisioningCompletedAccountRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedAccountRequestsInner from a JSON string
provisioning_completed_account_requests_inner_instance = ProvisioningCompletedAccountRequestsInner.from_json(json)
# print the JSON string representation of the object
print(ProvisioningCompletedAccountRequestsInner.to_json())

# convert the object into a dict
provisioning_completed_account_requests_inner_dict = provisioning_completed_account_requests_inner_instance.to_dict()
# create an instance of ProvisioningCompletedAccountRequestsInner from a dict
provisioning_completed_account_requests_inner_from_dict = ProvisioningCompletedAccountRequestsInner.from_dict(provisioning_completed_account_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


