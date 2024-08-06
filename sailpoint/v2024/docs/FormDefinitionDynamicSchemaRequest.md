# FormDefinitionDynamicSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FormDefinitionDynamicSchemaRequestAttributes**](FormDefinitionDynamicSchemaRequestAttributes.md) |  | [optional] 
**description** | **str** | Description is the form definition dynamic schema description text | [optional] 
**id** | **str** | ID is a unique identifier | [optional] 
**type** | **str** | Type is the form definition dynamic schema type | [optional] 
**version_number** | **int** | VersionNumber is the form definition dynamic schema version number | [optional] 

## Example

```python
from sailpoint.v2024.models.form_definition_dynamic_schema_request import FormDefinitionDynamicSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionDynamicSchemaRequest from a JSON string
form_definition_dynamic_schema_request_instance = FormDefinitionDynamicSchemaRequest.from_json(json)
# print the JSON string representation of the object
print FormDefinitionDynamicSchemaRequest.to_json()

# convert the object into a dict
form_definition_dynamic_schema_request_dict = form_definition_dynamic_schema_request_instance.to_dict()
# create an instance of FormDefinitionDynamicSchemaRequest from a dict
form_definition_dynamic_schema_request_form_dict = form_definition_dynamic_schema_request.from_dict(form_definition_dynamic_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


