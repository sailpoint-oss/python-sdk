# ConfigObject

Config export and import format for individual object configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Current version of configuration object. | [optional] 
**var_self** | [**SelfImportExportDto**](SelfImportExportDto.md) |  | [optional] 
**object** | **Dict[str, object]** | Object details. Format dependant on the object type. | [optional] 

## Example

```python
from sailpoint.beta.models.config_object import ConfigObject

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigObject from a JSON string
config_object_instance = ConfigObject.from_json(json)
# print the JSON string representation of the object
print ConfigObject.to_json()

# convert the object into a dict
config_object_dict = config_object_instance.to_dict()
# create an instance of ConfigObject from a dict
config_object_form_dict = config_object.from_dict(config_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


