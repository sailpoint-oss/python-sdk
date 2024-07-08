# CorrelationConfig

Source configuration information that is used by correlation process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the correlation configuration. | [optional] 
**name** | **str** | The name of the correlation configuration. | [optional] 
**attribute_assignments** | [**List[CorrelationConfigAttributeAssignmentsInner]**](CorrelationConfigAttributeAssignmentsInner.md) | The list of attribute assignments of the correlation configuration. | [optional] 

## Example

```python
from sailpoint.beta.models.correlation_config import CorrelationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationConfig from a JSON string
correlation_config_instance = CorrelationConfig.from_json(json)
# print the JSON string representation of the object
print CorrelationConfig.to_json()

# convert the object into a dict
correlation_config_dict = correlation_config_instance.to_dict()
# create an instance of CorrelationConfig from a dict
correlation_config_form_dict = correlation_config.from_dict(correlation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


