# SourceManagerCorrelationRule

Reference to the ManagerCorrelationRule, only used when a simple filter isn't sufficient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the rule | [optional] 
**name** | **str** | Human-readable display name of the rule | [optional] 

## Example

```python
from sailpoint.beta.models.source_manager_correlation_rule import SourceManagerCorrelationRule

# TODO update the JSON string below
json = "{}"
# create an instance of SourceManagerCorrelationRule from a JSON string
source_manager_correlation_rule_instance = SourceManagerCorrelationRule.from_json(json)
# print the JSON string representation of the object
print SourceManagerCorrelationRule.to_json()

# convert the object into a dict
source_manager_correlation_rule_dict = source_manager_correlation_rule_instance.to_dict()
# create an instance of SourceManagerCorrelationRule from a dict
source_manager_correlation_rule_form_dict = source_manager_correlation_rule.from_dict(source_manager_correlation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


