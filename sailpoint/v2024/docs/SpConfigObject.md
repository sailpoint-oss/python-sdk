# SpConfigObject

Response model for get object configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The object type this configuration is for. | [optional] 
**reference_extractors** | **List[str]** | List of json paths within an exported object of this type that represent references that need to be resolved. | [optional] 
**signature_required** | **bool** | If true, this type of object will be JWS signed and cannot be modified before import. | [optional] [default to False]
**always_resolve_by_id** | **bool** | Whether this object type has to be resolved always by ID | [optional] [default to False]
**legacy_object** | **bool** | Whether this is a legacy object | [optional] [default to False]
**one_per_tenant** | **bool** | Whether there is only one object of this type | [optional] [default to False]
**exportable** | **bool** | Whether this object can be exported or it is just a reference object | [optional] [default to False]
**rules** | [**SpConfigRules**](SpConfigRules.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.sp_config_object import SpConfigObject

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigObject from a JSON string
sp_config_object_instance = SpConfigObject.from_json(json)
# print the JSON string representation of the object
print(SpConfigObject.to_json())

# convert the object into a dict
sp_config_object_dict = sp_config_object_instance.to_dict()
# create an instance of SpConfigObject from a dict
sp_config_object_from_dict = SpConfigObject.from_dict(sp_config_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


