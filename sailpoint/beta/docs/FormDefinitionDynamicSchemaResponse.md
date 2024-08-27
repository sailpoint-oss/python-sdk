# FormDefinitionDynamicSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_schema** | **Dict[str, object]** | OutputSchema holds a JSON schema generated dynamically | [optional] 

## Example

```python
from sailpoint.beta.models.form_definition_dynamic_schema_response import FormDefinitionDynamicSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionDynamicSchemaResponse from a JSON string
form_definition_dynamic_schema_response_instance = FormDefinitionDynamicSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(FormDefinitionDynamicSchemaResponse.to_json())

# convert the object into a dict
form_definition_dynamic_schema_response_dict = form_definition_dynamic_schema_response_instance.to_dict()
# create an instance of FormDefinitionDynamicSchemaResponse from a dict
form_definition_dynamic_schema_response_from_dict = FormDefinitionDynamicSchemaResponse.from_dict(form_definition_dynamic_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


