# SourceManagerCorrelationRule

Reference to the ManagerCorrelationRule. Only use this rule when a simple filter isn't sufficient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Rule ID. | [optional] 
**name** | **str** | Rule&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v3.models.source_manager_correlation_rule import SourceManagerCorrelationRule

# TODO update the JSON string below
json = "{}"
# create an instance of SourceManagerCorrelationRule from a JSON string
source_manager_correlation_rule_instance = SourceManagerCorrelationRule.from_json(json)
# print the JSON string representation of the object
print(SourceManagerCorrelationRule.to_json())

# convert the object into a dict
source_manager_correlation_rule_dict = source_manager_correlation_rule_instance.to_dict()
# create an instance of SourceManagerCorrelationRule from a dict
source_manager_correlation_rule_from_dict = SourceManagerCorrelationRule.from_dict(source_manager_correlation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


