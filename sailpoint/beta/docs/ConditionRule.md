# ConditionRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Operator is a ConditionRuleComparisonOperatorType value EQ ConditionRuleComparisonOperatorTypeEquals  ConditionRuleComparisonOperatorTypeEquals is a comparison operator, the source and target are compared for equality NE ConditionRuleComparisonOperatorTypeNotEquals  ConditionRuleComparisonOperatorTypeNotEquals is a comparison operator, the source and target are compared for the opposite of equality CO ConditionRuleComparisonOperatorTypeContains  ConditionRuleComparisonOperatorTypeContains is a comparison operator, the source is searched to see if it contains the value NOT_CO ConditionRuleComparisonOperatorTypeNotContains IN ConditionRuleComparisonOperatorTypeIncludes  ConditionRuleComparisonOperatorTypeIncludes is a comparison operator, the source will be searched if it equals any of the values NOT_IN ConditionRuleComparisonOperatorTypeNotIncludes EM ConditionRuleComparisonOperatorTypeEmpty NOT_EM ConditionRuleComparisonOperatorTypeNotEmpty SW ConditionRuleComparisonOperatorTypeStartsWith  ConditionRuleComparisonOperatorTypeStartsWith checks if a string starts with another substring of the same string, this operator is case-sensitive NOT_SW ConditionRuleComparisonOperatorTypeNotStartsWith EW ConditionRuleComparisonOperatorTypeEndsWith  ConditionRuleComparisonOperatorTypeEndsWith checks if a string ends with another substring of the same string, this operator is case-sensitive NOT_EW ConditionRuleComparisonOperatorTypeNotEndsWith | [optional] 
**source** | **str** | Source, if the sourceType is ConditionRuleSourceTypeInput then the source type is the name of the form input to accept. While if the sourceType is ConditionRuleSourceTypeElement then source is the name of a technical key of an element to retrieve its value | [optional] 
**source_type** | **str** | SourceType defines what type of object is being selected. Either a reference to a form input (by input name), or a form element (by technical key) INPUT ConditionRuleSourceTypeInput ELEMENT ConditionRuleSourceTypeElement | [optional] 
**value** | **object** | Value is the value based on the ValueType | [optional] 
**value_type** | **str** | ValueType is a ConditionRuleValueType type STRING ConditionRuleValueTypeString  ConditionRuleValueTypeString the value field is a static string STRING_LIST ConditionRuleValueTypeStringList  ConditionRuleValueTypeStringList the value field is an array of string values INPUT ConditionRuleValueTypeInput  ConditionRuleValueTypeInput the value field is a reference to a form input by ELEMENT ConditionRuleValueTypeElement  ConditionRuleValueTypeElement the value field is a reference to form element (by technical key) LIST ConditionRuleValueTypeList BOOLEAN ConditionRuleValueTypeBoolean | [optional] 

## Example

```python
from beta.models.condition_rule import ConditionRule

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionRule from a JSON string
condition_rule_instance = ConditionRule.from_json(json)
# print the JSON string representation of the object
print ConditionRule.to_json()

# convert the object into a dict
condition_rule_dict = condition_rule_instance.to_dict()
# create an instance of ConditionRule from a dict
condition_rule_form_dict = condition_rule.from_dict(condition_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


