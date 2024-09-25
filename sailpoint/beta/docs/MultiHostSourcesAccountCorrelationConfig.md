# MultiHostSourcesAccountCorrelationConfig

Reference to account correlation config object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of object being referenced. | [optional] 
**id** | **str** | Account correlation config ID. | [optional] 
**name** | **str** | Account correlation config&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.multi_host_sources_account_correlation_config import MultiHostSourcesAccountCorrelationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostSourcesAccountCorrelationConfig from a JSON string
multi_host_sources_account_correlation_config_instance = MultiHostSourcesAccountCorrelationConfig.from_json(json)
# print the JSON string representation of the object
print(MultiHostSourcesAccountCorrelationConfig.to_json())

# convert the object into a dict
multi_host_sources_account_correlation_config_dict = multi_host_sources_account_correlation_config_instance.to_dict()
# create an instance of MultiHostSourcesAccountCorrelationConfig from a dict
multi_host_sources_account_correlation_config_from_dict = MultiHostSourcesAccountCorrelationConfig.from_dict(multi_host_sources_account_correlation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


