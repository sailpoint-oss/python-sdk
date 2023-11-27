# SpConfigObject

Response model for get object configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | The object type this configuration is for. | [optional] 
**resolve_by_id_url** | [**SpConfigUrl**](SpConfigUrl.md) |  | [optional] 
**resolve_by_name_url** | [**List[SpConfigUrl]**](SpConfigUrl.md) | Url and query parameters to be used to resolve this type of object by name. | [optional] 
**export_url** | [**SpConfigUrl**](SpConfigUrl.md) |  | [optional] 
**export_right** | **str** | Rights needed by the invoker of sp-config/export in order to export this type of object. | [optional] 
**export_limit** | **int** | Pagination limit imposed by the target service for this object type. | [optional] 
**import_url** | [**SpConfigUrl**](SpConfigUrl.md) |  | [optional] 
**import_right** | **str** | Rights needed by the invoker of sp-config/import in order to import this type of object. | [optional] 
**import_limit** | **int** | Pagination limit imposed by the target service for this object type. | [optional] 
**reference_extractors** | **List[str]** | List of json paths within an exported object of this type that represent references that need to be resolved. | [optional] 
**signature_required** | **bool** | If true, this type of object will be JWS signed and cannot be modified before import. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.sp_config_object import SpConfigObject

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigObject from a JSON string
sp_config_object_instance = SpConfigObject.from_json(json)
# print the JSON string representation of the object
print SpConfigObject.to_json()

# convert the object into a dict
sp_config_object_dict = sp_config_object_instance.to_dict()
# create an instance of SpConfigObject from a dict
sp_config_object_form_dict = sp_config_object.from_dict(sp_config_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


