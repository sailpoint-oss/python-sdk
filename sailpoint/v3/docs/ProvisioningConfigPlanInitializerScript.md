# ProvisioningConfigPlanInitializerScript

This is a reference to a plan initializer script.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | This is a Rule that allows provisioning instruction changes. | [optional] 

## Example

```python
from sailpoint.v3.models.provisioning_config_plan_initializer_script import ProvisioningConfigPlanInitializerScript

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfigPlanInitializerScript from a JSON string
provisioning_config_plan_initializer_script_instance = ProvisioningConfigPlanInitializerScript.from_json(json)
# print the JSON string representation of the object
print ProvisioningConfigPlanInitializerScript.to_json()

# convert the object into a dict
provisioning_config_plan_initializer_script_dict = provisioning_config_plan_initializer_script_instance.to_dict()
# create an instance of ProvisioningConfigPlanInitializerScript from a dict
provisioning_config_plan_initializer_script_form_dict = provisioning_config_plan_initializer_script.from_dict(provisioning_config_plan_initializer_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


