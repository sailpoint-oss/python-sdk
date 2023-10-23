# ProvisioningPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the provisioning policy name | 
**description** | **str** | the description of the provisioning policy | [optional] 
**usage_type** | [**UsageType**](UsageType.md) |  | [optional] 
**fields** | [**List[FieldDetailsDto]**](FieldDetailsDto.md) |  | [optional] 

## Example

```python
from v3.models.provisioning_policy import ProvisioningPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningPolicy from a JSON string
provisioning_policy_instance = ProvisioningPolicy.from_json(json)
# print the JSON string representation of the object
print ProvisioningPolicy.to_json()

# convert the object into a dict
provisioning_policy_dict = provisioning_policy_instance.to_dict()
# create an instance of ProvisioningPolicy from a dict
provisioning_policy_form_dict = provisioning_policy.from_dict(provisioning_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


