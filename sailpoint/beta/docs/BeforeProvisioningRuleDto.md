# BeforeProvisioningRuleDto

Before Provisioning Rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Before Provisioning Rule DTO type. | [optional] 
**id** | **str** | Before Provisioning Rule ID. | [optional] 
**name** | **str** | Rule display name. | [optional] 

## Example

```python
from sailpoint.beta.models.before_provisioning_rule_dto import BeforeProvisioningRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of BeforeProvisioningRuleDto from a JSON string
before_provisioning_rule_dto_instance = BeforeProvisioningRuleDto.from_json(json)
# print the JSON string representation of the object
print(BeforeProvisioningRuleDto.to_json())

# convert the object into a dict
before_provisioning_rule_dto_dict = before_provisioning_rule_dto_instance.to_dict()
# create an instance of BeforeProvisioningRuleDto from a dict
before_provisioning_rule_dto_from_dict = BeforeProvisioningRuleDto.from_dict(before_provisioning_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


