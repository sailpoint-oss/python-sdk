# JITConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The indicator for just-in-time provisioning enabled | [optional] [default to False]
**source_id** | **str** | the sourceId that mapped to just-in-time provisioning configuration | [optional] 
**source_attribute_mappings** | **Dict[str, str]** | A mapping of identity profile attribute names to SAML assertion attribute names | [optional] 

## Example

```python
from sailpoint.v3.models.jit_configuration import JITConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of JITConfiguration from a JSON string
jit_configuration_instance = JITConfiguration.from_json(json)
# print the JSON string representation of the object
print(JITConfiguration.to_json())

# convert the object into a dict
jit_configuration_dict = jit_configuration_instance.to_dict()
# create an instance of JITConfiguration from a dict
jit_configuration_from_dict = JITConfiguration.from_dict(jit_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


