# MultiHostSourcesManagerCorrelationRule

Reference to the ManagerCorrelationRule. Only use this rule when a simple filter isn't sufficient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Rule ID. | [optional] 
**name** | **str** | Rule&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_manager_correlation_rule import MultiHostSourcesManagerCorrelationRule

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesManagerCorrelationRule from a JSON string
multi_host_sources_manager_correlation_rule_instance = MultiHostSourcesManagerCorrelationRule.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesManagerCorrelationRule.to_json())

# convert the object into a dict
multi_host_sources_manager_correlation_rule_dict = multi_host_sources_manager_correlation_rule_instance.to_dict()
# create an instance of MultiHostSourcesManagerCorrelationRule from a dict
multi_host_sources_manager_correlation_rule_from_dict = MultiHostSourcesManagerCorrelationRule.from_dict(multi_host_sources_manager_correlation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


