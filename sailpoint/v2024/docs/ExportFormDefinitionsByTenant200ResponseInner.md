# ExportFormDefinitionsByTenant200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**FormDefinitionResponse**](FormDefinitionResponse.md) |  | [optional] 
**var_self** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.export_form_definitions_by_tenant200_response_inner import ExportFormDefinitionsByTenant200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExportFormDefinitionsByTenant200ResponseInner from a JSON string
export_form_definitions_by_tenant200_response_inner_instance = ExportFormDefinitionsByTenant200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ExportFormDefinitionsByTenant200ResponseInner.to_json())

# convert the object into a dict
export_form_definitions_by_tenant200_response_inner_dict = export_form_definitions_by_tenant200_response_inner_instance.to_dict()
# create an instance of ExportFormDefinitionsByTenant200ResponseInner from a dict
export_form_definitions_by_tenant200_response_inner_from_dict = ExportFormDefinitionsByTenant200ResponseInner.from_dict(export_form_definitions_by_tenant200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


