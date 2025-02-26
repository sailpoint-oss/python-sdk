# SpConfigRule

Format of Config Hub Object Rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | JSONPath expression denoting the path within the object where a value substitution should be applied | [optional] 
**value** | [**SpConfigRuleValue**](SpConfigRuleValue.md) |  | [optional] 
**modes** | **List[str]** | Draft modes to which this rule will apply | [optional] 

## Example

```python
from sailpoint.v2024.models.sp_config_rule import SpConfigRule

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigRule from a JSON string
sp_config_rule_instance = SpConfigRule.from_json(json)
# print the JSON string representation of the object
print(SpConfigRule.to_json())

# convert the object into a dict
sp_config_rule_dict = sp_config_rule_instance.to_dict()
# create an instance of SpConfigRule from a dict
sp_config_rule_from_dict = SpConfigRule.from_dict(sp_config_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


