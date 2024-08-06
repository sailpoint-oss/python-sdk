# ProvisioningPolicyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the provisioning policy name | 
**description** | **str** | the description of the provisioning policy | [optional] 
**usage_type** | [**UsageType**](UsageType.md) |  | [optional] 
**fields** | [**List[FieldDetailsDto]**](FieldDetailsDto.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.provisioning_policy_dto import ProvisioningPolicyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningPolicyDto from a JSON string
provisioning_policy_dto_instance = ProvisioningPolicyDto.from_json(json)
# print the JSON string representation of the object
print ProvisioningPolicyDto.to_json()

# convert the object into a dict
provisioning_policy_dto_dict = provisioning_policy_dto_instance.to_dict()
# create an instance of ProvisioningPolicyDto from a dict
provisioning_policy_dto_form_dict = provisioning_policy_dto.from_dict(provisioning_policy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


