# ProvisioningConfig1PlanInitializerScript

This is a reference to a plan initializer script.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | This is a Rule that allows provisioning instruction changes. | [optional] 

## Example

```python
from sailpoint.v2024.models.provisioning_config1_plan_initializer_script import ProvisioningConfig1PlanInitializerScript

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfig1PlanInitializerScript from a JSON string
provisioning_config1_plan_initializer_script_instance = ProvisioningConfig1PlanInitializerScript.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConfig1PlanInitializerScript.to_json())

# convert the object into a dict
provisioning_config1_plan_initializer_script_dict = provisioning_config1_plan_initializer_script_instance.to_dict()
# create an instance of ProvisioningConfig1PlanInitializerScript from a dict
provisioning_config1_plan_initializer_script_from_dict = ProvisioningConfig1PlanInitializerScript.from_dict(provisioning_config1_plan_initializer_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


