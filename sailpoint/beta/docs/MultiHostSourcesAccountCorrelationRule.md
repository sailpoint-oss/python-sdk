# MultiHostSourcesAccountCorrelationRule

Reference to a rule that can do COMPLEX correlation. Only use this rule when you can't use accountCorrelationConfig.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Rule ID. | [optional] 
**name** | **str** | Rule&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_account_correlation_rule import MultiHostSourcesAccountCorrelationRule

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesAccountCorrelationRule from a JSON string
multi_host_sources_account_correlation_rule_instance = MultiHostSourcesAccountCorrelationRule.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesAccountCorrelationRule.to_json())

# convert the object into a dict
multi_host_sources_account_correlation_rule_dict = multi_host_sources_account_correlation_rule_instance.to_dict()
# create an instance of MultiHostSourcesAccountCorrelationRule from a dict
multi_host_sources_account_correlation_rule_from_dict = MultiHostSourcesAccountCorrelationRule.from_dict(multi_host_sources_account_correlation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


