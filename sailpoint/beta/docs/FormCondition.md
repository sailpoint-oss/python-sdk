# FormCondition

Represent a form conditional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_operator** | **str** | ConditionRuleLogicalOperatorType value. AND ConditionRuleLogicalOperatorTypeAnd OR ConditionRuleLogicalOperatorTypeOr | [optional] 
**rules** | [**List[ConditionRule]**](ConditionRule.md) | List of rules. | [optional] 
**effects** | [**List[ConditionEffect]**](ConditionEffect.md) | List of effects. | [optional] 

## Example

```python
from sailpoint.beta.models.form_condition import FormCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FormCondition from a JSON string
form_condition_instance = FormCondition.from_json(json)
# print the JSON string representation of the object
print(FormCondition.to_json())

# convert the object into a dict
form_condition_dict = form_condition_instance.to_dict()
# create an instance of FormCondition from a dict
form_condition_from_dict = FormCondition.from_dict(form_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


