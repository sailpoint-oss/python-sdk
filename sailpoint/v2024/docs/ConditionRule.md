# ConditionRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | Defines the type of object being selected. It will be either a reference to a form input (by input name) or a form element (by technical key). INPUT ConditionRuleSourceTypeInput ELEMENT ConditionRuleSourceTypeElement | [optional] 
**source** | **str** | Source - if the sourceType is ConditionRuleSourceTypeInput, the source type is the name of the form input to accept. However, if the sourceType is ConditionRuleSourceTypeElement, the source is the name of a technical key of an element to retrieve its value. | [optional] 
**operator** | **str** | ConditionRuleComparisonOperatorType value. EQ ConditionRuleComparisonOperatorTypeEquals  This comparison operator compares the source and target for equality. NE ConditionRuleComparisonOperatorTypeNotEquals  This comparison operator compares the source and target for inequality. CO ConditionRuleComparisonOperatorTypeContains  This comparison operator searches the source to see whether it contains the value. NOT_CO ConditionRuleComparisonOperatorTypeNotContains IN ConditionRuleComparisonOperatorTypeIncludes  This comparison operator searches the source if it equals any of the values. NOT_IN ConditionRuleComparisonOperatorTypeNotIncludes EM ConditionRuleComparisonOperatorTypeEmpty NOT_EM ConditionRuleComparisonOperatorTypeNotEmpty SW ConditionRuleComparisonOperatorTypeStartsWith  Checks whether a string starts with another substring of the same string. This operator is case-sensitive. NOT_SW ConditionRuleComparisonOperatorTypeNotStartsWith EW ConditionRuleComparisonOperatorTypeEndsWith  Checks whether a string ends with another substring of the same string. This operator is case-sensitive. NOT_EW ConditionRuleComparisonOperatorTypeNotEndsWith | [optional] 
**value_type** | **str** | ConditionRuleValueType type. STRING ConditionRuleValueTypeString  This value is a static string. STRING_LIST ConditionRuleValueTypeStringList  This value is an array of string values. INPUT ConditionRuleValueTypeInput  This value is a reference to a form input. ELEMENT ConditionRuleValueTypeElement  This value is a reference to a form element (by technical key). LIST ConditionRuleValueTypeList BOOLEAN ConditionRuleValueTypeBoolean | [optional] 
**value** | **object** | Based on the ValueType. | [optional] 

## Example

```python
from sailpoint.v2024.models.condition_rule import ConditionRule

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionRule from a JSON string
condition_rule_instance = ConditionRule.from_json(json)
# print the JSON string representation of the object
print(ConditionRule.to_json())

# convert the object into a dict
condition_rule_dict = condition_rule_instance.to_dict()
# create an instance of ConditionRule from a dict
condition_rule_from_dict = ConditionRule.from_dict(condition_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


