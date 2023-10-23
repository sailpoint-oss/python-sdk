# FormCondition

FormCondition represent a form conditional

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effects** | [**List[ConditionEffect]**](ConditionEffect.md) | Effects is a list of effects | [optional] 
**rule_operator** | **str** | RuleOperator is a ConditionRuleLogicalOperatorType value AND ConditionRuleLogicalOperatorTypeAnd OR ConditionRuleLogicalOperatorTypeOr | [optional] 
**rules** | [**List[ConditionRule]**](ConditionRule.md) | Rules is a list of rules | [optional] 

## Example

```python
from beta.models.form_condition import FormCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FormCondition from a JSON string
form_condition_instance = FormCondition.from_json(json)
# print the JSON string representation of the object
print FormCondition.to_json()

# convert the object into a dict
form_condition_dict = form_condition_instance.to_dict()
# create an instance of FormCondition from a dict
form_condition_form_dict = form_condition.from_dict(form_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


