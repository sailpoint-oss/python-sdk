# ManagerCorrelationMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_attribute_name** | **str** | Name of the attribute to use for manager correlation. The value found on the account attribute will be used to lookup the manager&#39;s identity. | [optional] 
**identity_attribute_name** | **str** | Name of the identity attribute to search when trying to find a manager using the value from the accountAttribute. | [optional] 

## Example

```python
from sailpoint.beta.models.manager_correlation_mapping import ManagerCorrelationMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerCorrelationMapping from a JSON string
manager_correlation_mapping_instance = ManagerCorrelationMapping.from_json(json)
# print the JSON string representation of the object
print ManagerCorrelationMapping.to_json()

# convert the object into a dict
manager_correlation_mapping_dict = manager_correlation_mapping_instance.to_dict()
# create an instance of ManagerCorrelationMapping from a dict
manager_correlation_mapping_form_dict = manager_correlation_mapping.from_dict(manager_correlation_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


