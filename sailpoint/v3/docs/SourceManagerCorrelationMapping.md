# SourceManagerCorrelationMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_attribute_name** | **str** | Name of the attribute to use for manager correlation. The value found on the account attribute will be used to lookup the manager&#39;s identity. | [optional] 
**identity_attribute_name** | **str** | Name of the identity attribute to search when trying to find a manager using the value from the accountAttribute. | [optional] 

## Example

```python
from sailpoint.v3.models.source_manager_correlation_mapping import SourceManagerCorrelationMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SourceManagerCorrelationMapping from a JSON string
source_manager_correlation_mapping_instance = SourceManagerCorrelationMapping.from_json(json)
# print the JSON string representation of the object
print SourceManagerCorrelationMapping.to_json()

# convert the object into a dict
source_manager_correlation_mapping_dict = source_manager_correlation_mapping_instance.to_dict()
# create an instance of SourceManagerCorrelationMapping from a dict
source_manager_correlation_mapping_form_dict = source_manager_correlation_mapping.from_dict(source_manager_correlation_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


