# SpConfigRules

Rules to be applied to the config object during draft process

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**take_from_target_rules** | [**List[SpConfigRule]**](SpConfigRule.md) |  | [optional] 
**default_rules** | [**List[SpConfigRule]**](SpConfigRule.md) |  | [optional] 
**editable** | **bool** | Whether this object can be edited | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.sp_config_rules import SpConfigRules

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigRules from a JSON string
sp_config_rules_instance = SpConfigRules.from_json(json)
# print the JSON string representation of the object
print(SpConfigRules.to_json())

# convert the object into a dict
sp_config_rules_dict = sp_config_rules_instance.to_dict()
# create an instance of SpConfigRules from a dict
sp_config_rules_from_dict = SpConfigRules.from_dict(sp_config_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


