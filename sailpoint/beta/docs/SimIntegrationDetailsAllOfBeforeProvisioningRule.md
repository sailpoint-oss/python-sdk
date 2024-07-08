# SimIntegrationDetailsAllOfBeforeProvisioningRule

Before provisioning rule of integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the rule | [optional] 
**name** | **str** | Human-readable display name of the rule | [optional] 

## Example

```python
from sailpoint.beta.models.sim_integration_details_all_of_before_provisioning_rule import SimIntegrationDetailsAllOfBeforeProvisioningRule

# TODO update the JSON string below
json = "{}"
# create an instance of SimIntegrationDetailsAllOfBeforeProvisioningRule from a JSON string
sim_integration_details_all_of_before_provisioning_rule_instance = SimIntegrationDetailsAllOfBeforeProvisioningRule.from_json(json)
# print the JSON string representation of the object
print SimIntegrationDetailsAllOfBeforeProvisioningRule.to_json()

# convert the object into a dict
sim_integration_details_all_of_before_provisioning_rule_dict = sim_integration_details_all_of_before_provisioning_rule_instance.to_dict()
# create an instance of SimIntegrationDetailsAllOfBeforeProvisioningRule from a dict
sim_integration_details_all_of_before_provisioning_rule_form_dict = sim_integration_details_all_of_before_provisioning_rule.from_dict(sim_integration_details_all_of_before_provisioning_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


