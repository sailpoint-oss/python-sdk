# MultiHostIntegrationTemplateType

This represents a Multi-Host Integration template type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the type. | [optional] 
**type** | **str** | This is the type value for the type. | 
**script_name** | **str** | This is the scriptName attribute value for the type. | 

## Example

```python
from sailpoint.beta.models.multi_host_integration_template_type import MultiHostIntegrationTemplateType

# TODO update the JSON string below
json = "{}"
# create an instance of MultiHostIntegrationTemplateType from a JSON string
multi_host_integration_template_type_instance = MultiHostIntegrationTemplateType.from_json(json)
# print the JSON string representation of the object
print(MultiHostIntegrationTemplateType.to_json())

# convert the object into a dict
multi_host_integration_template_type_dict = multi_host_integration_template_type_instance.to_dict()
# create an instance of MultiHostIntegrationTemplateType from a dict
multi_host_integration_template_type_from_dict = MultiHostIntegrationTemplateType.from_dict(multi_host_integration_template_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


