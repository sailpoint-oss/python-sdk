# ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the attribute being provisioned. | 
**attribute_value** | **str** | The value of the attribute being provisioned. | [optional] 
**operation** | **object** | The operation to handle the attribute. | 

## Example

```python
from sailpoint.v2024.models.provisioning_completed_account_requests_inner_attribute_requests_inner import ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner from a JSON string
provisioning_completed_account_requests_inner_attribute_requests_inner_instance = ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner.from_json(json)
# print the JSON string representation of the object
print(ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner.to_json())

# convert the object into a dict
provisioning_completed_account_requests_inner_attribute_requests_inner_dict = provisioning_completed_account_requests_inner_attribute_requests_inner_instance.to_dict()
# create an instance of ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner from a dict
provisioning_completed_account_requests_inner_attribute_requests_inner_from_dict = ProvisioningCompletedAccountRequestsInnerAttributeRequestsInner.from_dict(provisioning_completed_account_requests_inner_attribute_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


