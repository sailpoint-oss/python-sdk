# CorrelationConfigAttributeAssignmentsInner

The attribute assignment of the correlation configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | The property of the attribute assignment. | [optional] 
**value** | **str** | The value of the attribute assignment. | [optional] 
**operation** | **str** | The operation of the attribute assignment. | [optional] 
**complex** | **bool** | Whether or not the it&#39;s a complex attribute assignment. | [optional] [default to False]
**ignore_case** | **bool** | Whether or not the attribute assignment should ignore case. | [optional] [default to False]
**match_mode** | **str** | The match mode of the attribute assignment. | [optional] 
**filter_string** | **str** | The filter string of the attribute assignment. | [optional] 

## Example

```python
from sailpoint.beta.models.correlation_config_attribute_assignments_inner import CorrelationConfigAttributeAssignmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationConfigAttributeAssignmentsInner from a JSON string
correlation_config_attribute_assignments_inner_instance = CorrelationConfigAttributeAssignmentsInner.from_json(json)
# print the JSON string representation of the object
print(CorrelationConfigAttributeAssignmentsInner.to_json())

# convert the object into a dict
correlation_config_attribute_assignments_inner_dict = correlation_config_attribute_assignments_inner_instance.to_dict()
# create an instance of CorrelationConfigAttributeAssignmentsInner from a dict
correlation_config_attribute_assignments_inner_from_dict = CorrelationConfigAttributeAssignmentsInner.from_dict(correlation_config_attribute_assignments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


