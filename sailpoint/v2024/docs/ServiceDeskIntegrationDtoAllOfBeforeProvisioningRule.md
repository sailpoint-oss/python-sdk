# ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Before Provisioning Rule DTO type. | [optional] 
**id** | **str** | Before Provisioning Rule ID. | [optional] 
**name** | **str** | Rule display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.service_desk_integration_dto_all_of_before_provisioning_rule import ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule from a JSON string
service_desk_integration_dto_all_of_before_provisioning_rule_instance = ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule.from_json(json)
# print the JSON string representation of the object
print ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule.to_json()

# convert the object into a dict
service_desk_integration_dto_all_of_before_provisioning_rule_dict = service_desk_integration_dto_all_of_before_provisioning_rule_instance.to_dict()
# create an instance of ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule from a dict
service_desk_integration_dto_all_of_before_provisioning_rule_form_dict = service_desk_integration_dto_all_of_before_provisioning_rule.from_dict(service_desk_integration_dto_all_of_before_provisioning_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


