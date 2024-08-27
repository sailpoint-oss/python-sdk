# ConfigType

Type of Reassignment Configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] 
**internal_name** | [**ConfigTypeEnumCamel**](ConfigTypeEnumCamel.md) |  | [optional] 
**internal_name_camel** | [**ConfigTypeEnum**](ConfigTypeEnum.md) |  | [optional] 
**display_name** | **str** | Human readable display name of the type to be shown on UI | [optional] 
**description** | **str** | Description of the type of work to be reassigned, displayed by the UI. | [optional] 

## Example

```python
from sailpoint.v2024.models.config_type import ConfigType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigType from a JSON string
config_type_instance = ConfigType.from_json(json)
# print the JSON string representation of the object
print(ConfigType.to_json())

# convert the object into a dict
config_type_dict = config_type_instance.to_dict()
# create an instance of ConfigType from a dict
config_type_from_dict = ConfigType.from_dict(config_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


